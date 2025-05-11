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
    ],
  },
];
