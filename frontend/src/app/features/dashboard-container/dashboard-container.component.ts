import { Component, HostListener, OnInit } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { AuthService } from '../../core/services/auth.service';
import { CommonModule } from '@angular/common';
import { PopoverModule } from 'primeng/popover';
import { AvatarModule } from 'primeng/avatar';
import { CardsService } from '../../core/services/cards.service';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-dashboard-container',
  imports: [
    ButtonModule,
    CommonModule,
    PopoverModule,
    AvatarModule,
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
  ],
  templateUrl: './dashboard-container.component.html',
  styleUrl: './dashboard-container.component.scss',
})
export class DashboardContainerComponent implements OnInit {
  isSidebarExpanded: boolean = true;
  isMobile: boolean = false;
  sidebarToggle: boolean = false;

  menuItems: any = [
    { label: 'Dashboard', icon: 'pi pi-chart-bar  ', path: 'dashboard' },
    { label: 'My Cards', icon: 'pi pi-credit-card', path: 'cards' },
    { label: 'New Transaction', icon: 'pi pi-plus', path: 'new-transaction' },
    { label: 'Payments', icon: 'pi pi-money-bill', path: 'payments' },
  ];

  constructor(
    private authService: AuthService,
    private cardsService: CardsService
  ) {}

  ngOnInit(): void {
    const windowWidth = window.innerWidth;
    this.isMobile = windowWidth < 640;
    this.isSidebarExpanded = windowWidth > 1280;
  }

  @HostListener('window:resize', ['$event'])
  onResize(event: Event) {
    const windowWidth = window.innerWidth;
    this.isSidebarExpanded = windowWidth > 1280;
    this.isMobile = windowWidth < 640;
  }

  onSignOut() {
    this.authService.logOut();
  }

  getSidebarWidth(): string {
    if (!this.isSidebarExpanded && this.isMobile) {
      return '0'; // Hidden on mobile
    }
    if (this.isSidebarExpanded && this.isMobile) {
      return '75%'; // Show on mobile
    }
    if (this.isSidebarExpanded && !this.isMobile) {
      return '32rem'; // Desktop full size (like w-128)
    }
    return '6rem'; // Collapsed width (like w-24)
  }

  getSidebarPadding(): string {
    if (this.isMobile && !this.isSidebarExpanded) {
      return '0';
    }
    return '1.25rem';
  }
}
