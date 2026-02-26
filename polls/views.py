from django.db.models import F, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import FormView

from polls.forms import QuestionForm
from polls.models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class AllQuestionsView(generic.ListView):
    template_name = 'polls/all.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.order_by('id')

class FrequencyView(generic.DetailView):
    model = Question
    template_name = 'polls/frequency.html'
        #Note: **kwargs pour capturer les params non connus a l'avance
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choices'] = self.object.get_choices()
        return context

class StatisticsView(generic.TemplateView):
    template_name = 'polls/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nb_questions = Question.objects.count()
        nb_choices = Choice.objects.count()
        total_votes = Choice.objects.aggregate(Sum('votes'))['votes__sum'] or 0

        context['nb_questions'] = nb_questions
        context['nb_choices'] = nb_choices
        context['total_votes'] = total_votes
        context['mean'] = round(total_votes / nb_questions, 2) if nb_questions > 0 else 0
        context['last_question'] = Question.objects.order_by('-pub_date').first()
        context['most_popular'] = Question.get_most_popular()
        context['least_popular'] = Question.get_least_popular()
        return context

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        #redisplay the form
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice !"},
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

"""
utilisation de commit = False pour ne pas sauvegarder en bdd immédiatement
"""
class AddQuestionView(FormView):
    template_name = 'polls/add.html'
    form_class = QuestionForm

    def form_valid(self, form):
        question = form.save(commit=False)
        question.pub_date = timezone.now()
        question.save()
        choices = [form.cleaned_data.get(f'choice_{i}') for i in range(1, 6)]
        for choice_text in choices:
            if choice_text:
                question.choice_set.create(choice_text=choice_text, votes=0)
        return redirect('polls:all')