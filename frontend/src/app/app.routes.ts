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
    loadChildren: () =>
      import('./features/dashboard-container/dashboard-container.routes').then(
        (r) => r.dashboardRoutes
      ),
  },
  { path: '**', redirectTo: '/dashboard', pathMatch: 'full' },
];
