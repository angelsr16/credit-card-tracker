export interface Transaction {
  user_id: number;
  card_id: number;
  description: string;
  amount: number;
  date: Date;
  installments: number;
  monthly_charge?: number;
  is_interest_free: boolean;
}
