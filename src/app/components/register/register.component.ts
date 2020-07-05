import { Component, OnInit } from '@angular/core';
import { User } from '../users/user.model';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  user: User

  constructor() { }

  ngOnInit() {
  }

  userModel = new User("", "", "", "", "")

}
