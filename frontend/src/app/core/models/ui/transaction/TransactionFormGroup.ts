import { FormControl } from '@angular/forms';

export interface TransactionFormGroup {
  description: FormControl<string>;
  amount: FormControl<number>;
  date: FormControl<Date>;
  installments: FormControl<number>;
  monthly_charge: FormControl<number>;
  is_interest_free: FormControl<boolean>;
}
