export interface TransactionForm {
  description: string;
  amount: number;
  date: Date;
  installments: number;
  monthly_charge: number;
  is_interest_free: boolean;
}
