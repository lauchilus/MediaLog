import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { IBook } from '../models/book';

@Injectable({
  providedIn: 'root'
})
export class BooksService {
  
  BASE_URL = 'http://127.0.0.1:8000/';

  constructor(private httpClient: HttpClient, private route: Router) { }


  GetBooksList(){
    return this.httpClient.get<IBook[]>(`${this.BASE_URL}book/list/`)
  }

}
