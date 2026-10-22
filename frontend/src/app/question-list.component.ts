import { Component, effect, inject, signal, untracked } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { PollService } from './poll.service';
import { AuthService } from './auth.service';
import { Question } from './models';

@Component({selector: 'app-question-list',standalone: true,imports: [FormsModule],
  template: `
    @for (q of questions(); track q.id) {
      <div class="card mb-3">
        <div class="card-body">
          <h5 class="card-title">{{ q.question_text }}</h5>
          @for (c of q.choices; track c.id) {
            <div class="form-check">
              <input class="form-check-input" type="radio" [name]="'q' + q.id"
                     [id]="'c' + c.id" [value]="c.id" [(ngModel)]="selected[q.id]">
              <label class="form-check-label" [for]="'c' + c.id">
                {{ c.choice_text }}
                @if (c.votes !== undefined) {
                  <span class="badge text-bg-secondary ms-1">{{ c.votes }}</span>
                }
              </label>
            </div>
          }
          <button class="btn btn-primary btn-sm mt-2"
                  [disabled]="!selected[q.id]" (click)="vote(q.id)">Voter</button>
           @if (feedback(); as f) {
            @if (f.id === q.id) {
              <div class="alert mt-2 mb-0 py-2" [class.alert-success]="f.ok" [class.alert-danger]="!f.ok">
                {{ f.text }}
              </div>
            }
          }
        </div>
      </div>
    } @empty {
      <p class="text-muted">Aucun sondage pour le moment</p>
    }
  `,
})
/**
 * Component responsible for displaying the list of questions/polls and handling votes
 */
export class QuestionListComponent {
  private polls = inject(PollService);
  private auth = inject(AuthService);
  questions = signal<Question[]>([]);
  selected: Record<number, number> = {};

  constructor() {
    effect(() => {
      this.auth.isLoggedIn();
       // fetch questions without subscribing this effect to internal signals inside load()
      untracked(() => this.load());
    });
  }

  load() {
    this.polls.list().subscribe(qs => this.questions.set(qs));
  }

  feedback = signal<{
    id: number;
    text: string;
    ok: boolean
  } | null>(null);

  /**
   * Submits a user vote for a specific question ID using the selected choice
   * @param id - The id of the question
   */
  vote(id: number) {
    this.polls.vote(id, this.selected[id]).subscribe({
      next: () => {
        delete this.selected[id];
        this.show(id, 'Merci, votre vote a été enregistré', true);
        this.load();
      },
      error: e => this.show(id, e.error?.detail ?? 'Erreur lors du vote', false),
    });
  }

  /**
   * Helper for feedback
   */
  private show(id: number, text: string, ok: boolean) {
    this.feedback.set({ id, text, ok });
    setTimeout(() => this.feedback.set(null), 3000);
  }
}
