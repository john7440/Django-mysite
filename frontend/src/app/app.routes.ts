import { inject } from '@angular/core';
import { Router, Routes } from '@angular/router';
import { AuthService } from './auth.service';
import { QuestionListComponent } from './question-list.component';
import { LoginComponent } from './login.component';
import { AddQuestionComponent } from './add-question.component';

export const routes: Routes = [
  { path: '', component: QuestionListComponent },
  { path: 'login', component: LoginComponent },
  { path: 'add',component: AddQuestionComponent,
    canActivate: [() => inject(AuthService).isLoggedIn() || inject(Router).createUrlTree(['/login'])],},
];
