import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GamesService {

  BASE_URL = 'http://127.0.0.1:8000/';

  constructor(private httpClient: HttpClient) { }


  GetGamesList(){
    return this.httpClient.get<any>(`${this.BASE_URL}game/list/`)
  }
}
