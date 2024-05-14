import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AnimeService {

  BASE_URL = 'http://127.0.0.1:8000/';

  constructor(private httpClient: HttpClient) { }


  GetAnimeList(){
    return this.httpClient.get<any>(`${this.BASE_URL}anime/list/`)
  }
}
