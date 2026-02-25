from django.db.models import F, Sum
from django.http import HttpResponse, Http404, HttpResponseRedirect  # type: ignore
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


from polls.models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def all_questions(request):
    questions = Question.objects.order_by('id')
    return render(request, 'polls/all.html', {'questions': questions})

def frequency(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.get_choices()
    return render(request, 'polls/frequency.html', {'question': question, 'choices': choices})

def statistics(request):
    from polls.models import Question, Choice
    nb_questions = Question.objects.count()
    nb_choices = Choice.objects.count()
    total_votes = Choice.objects.aggregate(Sum('votes'))['votes__sum'] or 0
    mean = round(total_votes / nb_questions, 2) if nb_questions > 0 else 0
    last_question = Question.objects.order_by('-pub_date')[0]

    return render(request, 'polls/statistics.html',{
        'nb_questions': nb_questions,
        'nb_choices': nb_choices,
        'total_votes': total_votes,
        'mean': mean,
        'last_question': last_question,
    })


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