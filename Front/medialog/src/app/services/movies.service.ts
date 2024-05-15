import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MoviesService {
  BASE_URL = 'http://127.0.0.1:8000/';

  constructor(private httpClient: HttpClient) { }


  GetMoviesList(){
    return this.httpClient.get<any>(`${this.BASE_URL}movie/list/`)
  }


  GetMoviesSearch(movie: string,page: number){
    return this.httpClient.get<any>(`${this.BASE_URL}movie/search/?q=${movie}&page=${page}`)
  }
}

