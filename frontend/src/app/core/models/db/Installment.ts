export interface Installment {
  number: number;
  due_date: Date;
  amount_due: number;
  amount_paid: number;
  is_paid: boolean;
}
