import { Component, OnInit } from '@angular/core';
import { User } from '../users/user.model';
import { NgForm } from '@angular/forms';
import { UserService } from '../users/user.service'

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  user: User

  constructor(private userService: UserService) { }

  ngOnInit() {
  }
// empty user input fields - Firstname, Lastname, Email, Username, Password
  userModel = new User("", "", "", "", "")

  onSubmit() {
    console.log(this.userModel)
    this.userService.registerUser(this.userModel)
      .subscribe(data => console.log('success', data), error => console.error('error!', error)
      )
  }

}
