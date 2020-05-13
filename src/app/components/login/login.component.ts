import { Component, OnInit } from '@angular/core';
import { User } from '../users/user.model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  user: User

  constructor() { }

  ngOnInit(): void {
  }

}
