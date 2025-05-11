import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { BehaviorSubject, catchError, Observable } from 'rxjs';
import { Card } from '../models/db/Card';

@Injectable({
  providedIn: 'root',
})
export class CardsService {
  cardsSubject: BehaviorSubject<Card[]> = new BehaviorSubject<Card[]>([]);
  cards$: Observable<Card[]> = this.cardsSubject.asObservable();

  constructor(private http: HttpClient) {
    this.getCards().subscribe({
      next: (data) => {
        this.cardsSubject.next(data as Card[]);
      },
      error: (err) => {},
    });
  }

  getCards() {
    return this.http.get(`${environment.apiUrl}/cards`);
  }
}
