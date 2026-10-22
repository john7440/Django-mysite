import { Injectable, computed, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs';
import { API } from './api';

/**
 * Service responsible for managing user authentication, token storage, and login state
 */
@Injectable({ providedIn: 'root' })
export class AuthService {
  private http = inject(HttpClient);
  token = signal<string | null>(localStorage.getItem('access'));
  isLoggedIn = computed(() => !!this.token());

  /**
   * Authenticates the user with username and pass
   *  On success, stores the access token in localStorage and updates the reactive signal
   */
  login(username: string, password: string) {
    return this.http.post<{ access: string; refresh: string }>(`${API}/token/`, { username, password })
      .pipe(tap(response => {
        localStorage.setItem('access', response.access);
        this.token.set(response.access);
      }));
  }

  /**
   * Logs out the user by clearing the token from local storage and resetting the signal state
   */
  logout() {
    localStorage.removeItem('access');
    this.token.set(null);
  }
}
