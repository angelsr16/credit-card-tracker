import { Component, HostListener, OnInit } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { AuthService } from '../../core/services/auth.service';
import { CommonModule } from '@angular/common';
import { PopoverModule } from 'primeng/popover';
import { AvatarModule } from 'primeng/avatar';

@Component({
  selector: 'app-dashboard',
  imports: [ButtonModule, CommonModule, PopoverModule, AvatarModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss',
})
export class DashboardComponent implements OnInit {
  isSidebarExpanded: boolean = true;
  isMobile: boolean = false;
  sidebarToggle: boolean = false;

  constructor(private authService: AuthService) {}

  ngOnInit(): void {
    const windowWidth = window.innerWidth;
    this.isMobile = windowWidth < 640;
    this.isSidebarExpanded = windowWidth > 768;
  }

  @HostListener('window:resize', ['$event'])
  onResize(event: Event) {
    const windowWidth = window.innerWidth;
    this.isSidebarExpanded = windowWidth > 768;
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
