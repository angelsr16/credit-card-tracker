import { Routes } from '@angular/router';
import { AuthGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  {
    path: 'login',

    loadComponent: () =>
      import('./features/auth/login/login.component').then(
        (c) => c.LoginComponent
      ),
  },
  {
    path: 'dashboard',
    canActivate: [AuthGuard],
    loadComponent: () =>
      import('./features/dashboard/dashboard.component').then(
        (c) => c.DashboardComponent
      ),
  },
  { path: '**', redirectTo: '/dashboard', pathMatch: 'full' },
];
