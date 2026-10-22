import { Component, inject } from '@angular/core';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  template: `
    <nav class="navbar navbar-expand bg-body-tertiary mb-4">
      <div class="container">
        <a class="navbar-brand" routerLink="/">Sondages</a>
        <div class="navbar-nav ms-auto">
          @if (auth.isLoggedIn()) {
            <a class="nav-link" routerLink="/add">Ajouter</a>
            <a class="nav-link" href="#" (click)="logout($event)">Déconnexion</a>
          } @else {
            <a class="nav-link" routerLink="/login">Connexion</a>
          }
        </div>
      </div>
    </nav>
    <div class="container"><router-outlet /></div>
  `,
})

export class App {
  auth = inject(AuthService);
  private readonly router = inject(Router);

  logout(e: Event) {
    e.preventDefault();
    this.auth.logout();
    this.router.navigate(['/']);
  }
}
