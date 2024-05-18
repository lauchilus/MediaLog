import { Component, OnInit } from '@angular/core';
import { AnimeService } from '../../services/anime.service';
import { ActivatedRoute } from '@angular/router';
import { Anime } from '../../models/anime';
import { IBook } from '../../models/book';
import { Movie } from '../../models/movie';
import { BooksService } from '../../services/books.service';
import { GamesService } from '../../services/games.service';
import { MoviesService } from '../../services/movies.service';
import { SeriesService } from '../../services/series.service';

@Component({
  selector: 'app-details',
  standalone: true,
  imports: [],
  templateUrl: './details.component.html',
  styleUrl: './details.component.css'
})
export class DetailsComponent implements OnInit {

  search!: string;
  type !: string
  animeDetails!: AnimeDetails;

  constructor(private activatedRoute: ActivatedRoute,private bookService: BooksService, private movieService: MoviesService, private animeService: AnimeService, private serieService: SeriesService, private gamesService: GamesService){}

  ngOnInit(): void {
    this.activatedRoute.paramMap.subscribe(params => {
      this.search = params.get('id')!;
      this.type = params.get('type')!; 
    });
    this.SearchDetails();
  }

  SearchDetails(){
    switch (this.type) {
      case 'Books':
        if (this.search.length !== 0) {
          
        }
        break;
      case 'Movies':
        if (this.search.length !== 0) {
          
        }
        break;
      case 'Series':
        if (this.search.length !== 0) {
          
        }
        break;
      case 'anime':
        
        
          this.animeService.GetAnimeDetails(this.search).subscribe(
            (res: any) => {
              this.animeDetails = res
              console.log(res)
            }
          );

         
        break;
      case 'Games':
        if (this.search.length !== 0) {
          
        } 
        break;
      default:
        console.log("aa")
        break;
    }
  }

}

export interface AnimeDetails {
  id: number
  title: string
  main_picture: MainPicture
  start_date: string
  end_date: string
  synopsis: string
}

export interface MainPicture {
  medium: string
  large: string
}