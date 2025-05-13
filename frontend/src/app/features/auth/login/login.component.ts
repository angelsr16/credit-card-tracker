import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormControl,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { PasswordModule } from 'primeng/password';
import { ToastModule } from 'primeng/toast';
import { ButtonModule } from 'primeng/button';
import { MessageService } from 'primeng/api';
import { Router, RouterLink } from '@angular/router';
import { LoginFormGroup } from '../../../core/models/ui/login/LoginFormGroup';
import { LoginForm } from '../../../core/models/ui/login/LoginForm';
import { AuthService } from '../../../core/services/auth.service';

@Component({
  selector: 'app-login',
  imports: [
    FormsModule,
    ReactiveFormsModule,
    InputTextModule,
    PasswordModule,
    ToastModule,
    ButtonModule,
  ],
  providers: [MessageService],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
})
export class LoginComponent implements OnInit {
  loginFormGroup!: FormGroup<LoginFormGroup>;

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit() {
    if (this.authService.isAuthenticated()) {
      console.log("IS AUTH")
      this.router.navigate(['/dashboard']);
    }
    this.resetLoginFormGroup();
  }

  resetLoginFormGroup() {
    this.loginFormGroup = this.formBuilder.group<LoginFormGroup>({
      username: new FormControl('', {
        nonNullable: true,
        validators: [Validators.required],
      }),
      password: new FormControl('', {
        nonNullable: true,
        validators: [Validators.required],
      }),
    });
  }

  onLoginSubmit() {
    const loginData: LoginForm = this.loginFormGroup.getRawValue();

    this.authService.login(loginData).subscribe({
      next: (res) => {
        console.log('Authorized');
        this.authService.setToken(res.access_token);
        this.router.navigate(['/dashboard']);
      },
      error: (err) => {
        console.log(err);
        console.log('Invalid credentials.');
      },
    });
  }
}
