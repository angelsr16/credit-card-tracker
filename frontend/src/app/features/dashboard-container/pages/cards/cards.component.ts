import { Component } from '@angular/core';
import { CardsService } from '../../../../core/services/cards.service';
import { Card } from '../../../../core/models/db/Card';
import { CommonModule } from '@angular/common';
import { ColorPickerModule } from 'primeng/colorpicker';
import { FormsModule } from '@angular/forms';
import { GetGradientStylePipe } from '../../../../shared/pipes/get-gradient-style.pipe';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-cards',
  imports: [
    CommonModule,
    ColorPickerModule,
    FormsModule,
    GetGradientStylePipe,
    ButtonModule,
  ],
  templateUrl: './cards.component.html',
  styleUrl: './cards.component.scss',
})
export class CardsComponent {
  cards: Card[] = [];
  userColor = '#3498db'; // Example; set this based on user input

  constructor(private cardsService: CardsService) {
    this.cardsService.cards$.subscribe((data) => {
      this.cards = data as Card[];
    });
  }
}
