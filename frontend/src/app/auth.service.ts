import { Injectable, computed, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs';
import { API } from './api';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private http = inject(HttpClient);
  token = signal<string | null>(localStorage.getItem('access'));
  isLoggedIn = computed(() => !!this.token());

  login(username: string, password: string) {
    return this.http.post<{ access: string; refresh: string }>(`${API}/token/`, { username, password })
      .pipe(tap(r => {
        localStorage.setItem('access', r.access);
        this.token.set(r.access);
      }));
  }

  logout() {
    localStorage.removeItem('access');
    this.token.set(null);
  }
}
