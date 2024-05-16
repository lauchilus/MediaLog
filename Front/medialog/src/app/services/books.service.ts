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


  GetBooksList(page: number = 1){
    return this.httpClient.get<IBook[]>(`${this.BASE_URL}book/list/?page=${page}`)
  }

  GetBooksSearch(search: string, page: number){
    return this.httpClient.get<any>(`${this.BASE_URL}book/search/?q=${search}&page=${page}`)
  }

}


