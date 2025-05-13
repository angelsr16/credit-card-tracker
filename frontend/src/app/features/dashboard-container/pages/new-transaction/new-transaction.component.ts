import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormControl,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { TransactionFormGroup } from '../../../../core/models/ui/transaction/TransactionFormGroup';
import { SelectModule } from 'primeng/select';
import { CardsService } from '../../../../core/services/cards.service';
import { Card } from '../../../../core/models/db/Card';
import { InputNumberModule } from 'primeng/inputnumber';
import { DatePickerModule } from 'primeng/datepicker';
import { InputTextModule } from 'primeng/inputtext';
import { Installment } from '../../../../core/models/db/Installment';
import { TransactionForm } from '../../../../core/models/ui/transaction/TransactionForm';
import { addMonths } from '../../../../shared/utils/date-utils';
import { DatePipe, DecimalPipe } from '@angular/common';
import { TableModule } from 'primeng/table';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-new-transaction',
  imports: [
    FormsModule,
    ReactiveFormsModule,
    SelectModule,
    InputNumberModule,
    DatePickerModule,
    InputTextModule,
    DatePipe,
    DecimalPipe,
    TableModule,
    ButtonModule,
  ],
  templateUrl: './new-transaction.component.html',
  styleUrl: './new-transaction.component.scss',
})
export class NewTransactionComponent implements OnInit {
  cards: Card[] = [];
  transactionFormGroup!: FormGroup<TransactionFormGroup>;

  installments: Installment[] = [];

  selectedCard!: Card;

  constructor(
    private formBuilder: FormBuilder,
    private cardsService: CardsService
  ) {
    this.cardsService.cards$.subscribe((data) => {
      this.cards = data as Card[];
    });
  }

  ngOnInit(): void {
    this.transactionFormGroup = this.formBuilder.group<TransactionFormGroup>({
      description: new FormControl('', {
        nonNullable: true,
        validators: [Validators.required],
      }),
      amount: new FormControl(0.01, {
        nonNullable: true,
        validators: [Validators.required],
      }),
      date: new FormControl(new Date(), {
        nonNullable: true,
        validators: [Validators.required],
      }),
      installments: new FormControl(1, {
        nonNullable: true,
        validators: [Validators.required, Validators.min(1)],
      }),
      monthly_charge: new FormControl(0.01, {
        nonNullable: true,
        validators: [Validators.required, Validators.min(0.01)],
      }),
      is_interest_free: new FormControl(true, {
        nonNullable: true,
        validators: [Validators.required],
      }),
    });

    this.transactionFormGroup.valueChanges.subscribe((rawValue) => {
      if (this.selectedCard) {
        this.calculateInstallments(rawValue, this.selectedCard);
      }

      this.transactionFormGroup
        .get('amount')
        ?.setValue(
          (rawValue.monthly_charge ? rawValue.monthly_charge : 0.01) *
            (rawValue.installments ? rawValue.installments : 1)
        );
    });
  }

  onCardSelected() {
    console.log(this.selectedCard);

    var [year, month, day] = this.selectedCard.cut_off_date
      .toString()
      .split('-')
      .map(Number);
    this.selectedCard.cut_off_date = new Date(year, month - 1, day);

    var [year, month, day] = this.selectedCard.due_date
      .toString()
      .split('-')
      .map(Number);
    this.selectedCard.due_date = new Date(year, month - 1, day);

    this.calculateInstallments(
      this.transactionFormGroup.getRawValue(),
      this.selectedCard
    );
  }

  calculateInstallments(
    transactionValue: Partial<TransactionForm>,
    card: Card
  ) {
    const installmentsCount: number =
      transactionValue.installments !== undefined
        ? transactionValue.installments
        : 1;

    const installmentsList: Installment[] = [];
    for (let i = 0; i < installmentsCount; i++) {
      const newDueDate = addMonths(card.due_date, i + 1);
      const amountDue = transactionValue.monthly_charge
        ? transactionValue.monthly_charge
        : 0.01;

      installmentsList.push({
        number: i + 1,
        due_date: newDueDate,
        amount_due: amountDue,
        amount_paid: 0,
        is_paid: false,
      });
    }

    this.installments = [...installmentsList];
  }
}
