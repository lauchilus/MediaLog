import { HttpClient, HttpHeaders } from '@angular/common/http';
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

  GetAnimeSearch(search: string){
    return this.httpClient.get<any>(`${this.BASE_URL}anime/search/?q=${search}`)
  }

  ChangePage(url: string){
    return this.httpClient.post<any>(`${this.BASE_URL}anime/search/change_page`,{url: url})
  }
  
  GetAnimeDetails(q: string){
    return this.httpClient.get<any>(`${this.BASE_URL}anime/detail/?q=${q}`)
  }


}
