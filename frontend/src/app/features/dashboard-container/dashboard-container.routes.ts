import { Routes } from '@angular/router';
import { DashboardContainerComponent } from './dashboard-container.component';

export const dashboardRoutes: Routes = [
  {
    path: '',
    component: DashboardContainerComponent,
    children: [
      { path: '', redirectTo: 'cards', pathMatch: 'full' },
      {
        path: 'cards',
        loadComponent: () =>
          import('./pages/cards/cards.component').then((c) => c.CardsComponent),
      },
      {
        path: 'dashboard',
        loadComponent: () =>
          import('./pages/dashboard/dashboard.component').then(
            (c) => c.DashboardComponent
          ),
      },
      {
        path: 'new-transaction',
        loadComponent: () =>
          import('./pages/new-transaction/new-transaction.component').then(
            (c) => c.NewTransactionComponent
          ),
      },
      {
        path: 'payments',
        loadComponent: () =>
          import('./pages/payments/payments.component').then(
            (c) => c.PaymentsComponent
          ),
      },
    ],
  },
];
