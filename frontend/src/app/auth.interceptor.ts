import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { catchError, throwError } from 'rxjs';
import { AuthService } from './auth.service';

/**
 * Http Interceptor that automatically attaches an Authorization header
 * with a JWT Bearer token
 *
 * @param req - The outgoing HttpRequest object to be inspected/modified
 * @param next - The HttpHandlerFn used to pass the request to the next interceptor or backend
 * @returns An Observable emiting the HTTP event stream
 */
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const auth = inject(AuthService);
  const token = auth.token();
  const authReq = token ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } }) : req;
  return next(authReq).pipe(
    catchError(err => {
      if (err.status === 401 && token) auth.logout();
      return throwError(() => err);
    })
  );
};
