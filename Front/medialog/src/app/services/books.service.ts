import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BooksService {
  
  BASE_URL = 'http://127.0.0.1:8000/';

  constructor(private httpClient: HttpClient, private route: Router) { }


  GetBooksList(): Observable<any>{
    return this.httpClient.get(`${this.BASE_URL}book/list/`)
  }

}
