import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from './user.model';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  _url = ''
  constructor(private _http: HttpClient) {  }

  registerUser(user: User) {
    return this._http.post<any>(this._url, user)
  }
}
