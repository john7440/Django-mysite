import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from './auth.service';

@Component({selector: 'app-login',standalone: true,imports: [FormsModule],
  template: `
    <form class="col-md-4 mx-auto" (ngSubmit)="submit()">
      <h4 class="mb-3">Connexion</h4>
      <input class="form-control mb-2" name="u" placeholder="Utilisateur" [(ngModel)]="username">
      <input class="form-control mb-2" name="p" type="password" placeholder="Mot de passe" [(ngModel)]="password">
      @if (error()) { <div class="alert alert-danger">{{ error() }}</div> }
      <button class="btn btn-primary w-100">Se connecter</button>
    </form>
  `,
})
/**
 * Component responsible for managing the user login form and authentication
 */
export class LoginComponent {
  private readonly auth = inject(AuthService);
  private readonly router = inject(Router);
  username = '';
  password = '';
  error = signal('');

  submit() {
    this.auth.login(this.username, this.password).subscribe({
      next: () => this.router.navigate(['/']),
      error: () => this.error.set('Identifiants invalides'),
    });
  }
}
