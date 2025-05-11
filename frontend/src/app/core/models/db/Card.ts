export interface Card {
  id: number;
  user_id: number;  
  name: string;
  bank: string;
  created_at: Date;
  cut_off_date: Date;
  due_date: Date;
  limit: number;
  balance: number;
}
