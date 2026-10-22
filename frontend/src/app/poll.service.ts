import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API } from './api';
import { Question } from './models';

@Injectable({ providedIn: 'root' })
export class PollService {
  private readonly http = inject(HttpClient);

  list() {
    return this.http.get<Question[]>(`${API}/questions/`);
  }

  vote(id: number, choice: number) {
    return this.http.post(`${API}/questions/${id}/vote/`, {choice});
  }

  create(question_text: string, choices: string[]) {
    return this.http.post<Question>(`${API}/questions/`, {question_text, choices});
  }
}
