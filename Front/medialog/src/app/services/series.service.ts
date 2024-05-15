import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SeriesService {

  BASE_URL = 'http://127.0.0.1:8000/';

  constructor(private httpClient: HttpClient) { }


  GetSeriesList(){
    return this.httpClient.get<any>(`${this.BASE_URL}serie/list/`)
  }

  GetSeriesSearch(serie: string,page: number){
    return this.httpClient.get<any>(`${this.BASE_URL}serie/search/?q=${serie}&page=${page}`)
  }
}
