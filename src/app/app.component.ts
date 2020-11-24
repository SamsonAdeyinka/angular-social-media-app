import { Component } from '@angular/core';
import { HttpClient } from "@angular/common/http";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'social-media-project';

  readonly ROOT_URL = 'http://127.0.0.1:5000'

  user: any;

  constructor(private http: HttpClient) {}

  getUser() {
    this.user = this.http.get(this.ROOT_URL + '/api/users')
  }
}
