import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { PollService } from './poll.service';

@Component({ selector: 'app-add-question',standalone: true,imports: [FormsModule],
  template: `
    <form class="col-md-6 mx-auto" (ngSubmit)="submit()">
      <h4 class="mb-3">Nouveau sondage</h4>
      <input class="form-control mb-2" name="t" placeholder="Question" [(ngModel)]="text">
      <textarea class="form-control mb-2" name="c" rows="5"
                placeholder="Un choix par ligne (2 minimum)" [(ngModel)]="choicesText"></textarea>
      @if (error()) { <div class="alert alert-danger">{{ error() }}</div> }
      <button class="btn btn-success w-100">Créer</button>
    </form>
  `,
})
export class AddQuestionComponent {
  private polls = inject(PollService);
  private router = inject(Router);
  text = '';
  choicesText = '';
  error = signal('');

  submit() {
    const choices = this.choicesText.split('\n').map(s => s.trim()).filter(Boolean);
    this.polls.create(this.text, choices).subscribe({
      next: () => this.router.navigate(['/']),
      error: e => this.error.set(JSON.stringify(e.error)),
    });
  }
}
