import { Component, OnInit } from '@angular/core';
import { BooksService } from '../../services/books.service';
import { IBook } from '../../models/book';
import { CarrouselComponent } from "../carrousel/carrousel.component";
import { MoviesService } from '../../services/movies.service';
import { Movie } from '../../models/movie';
import { Anime } from '../../models/anime';
import { AnimeService } from '../../services/anime.service';
import { SeriesService } from '../../services/series.service';
import { GamesService } from '../../services/games.service';
import { forkJoin, map } from 'rxjs';

@Component({
    selector: 'app-home',
    standalone: true,
    templateUrl: './home.component.html',
    styleUrl: './home.component.css',
    imports: [CarrouselComponent]
})
export class HomeComponent implements OnInit{
  books: IBook[] = [];
  movies: Movie[] = [];
  series: Movie[] = [];
  animes: Anime[] = [];
  games: Movie[] = [];

  sources =[ 
    this.bookService.GetBooksList(),
    this.movieService.GetMoviesList(),
    this.serieService.GetSeriesList(),
    this.animeService.GetAnimeList(),
    this.gamesService.GetGamesList()
  ];

  constructor(private bookService: BooksService,private movieService: MoviesService,private animeService: AnimeService,private serieService: SeriesService,private gamesService: GamesService) { }

  ngOnInit(): void {
    forkJoin(this.sources)
    .pipe(
      map(([books,movies,series,animes,games]) =>{
        return {books,movies,series,animes,games}
      })
    ).subscribe((res:any)=>{
      console.log(res)
      this.books = res.books as IBook[],
      this.movies = res.movies.movies as Movie[],
      this.series = res.series.movies as Movie[],
      this.animes = res.animes.data as Anime[],
      this.games = res.games as Movie[]
    })
  }

  getItems(): void {
    this.bookService.GetBooksList().subscribe(
      (data) => {
        this.books = data.map((book: IBook)=>{
          return{
            ...book,
          }
          
        })
        console.log(this.books)        
        });
      }
    
  

  getMovies(): void {
    this.movieService.GetMoviesList().subscribe(
      (data) => {
        this.movies = data.movies
        console.log(this.movies)        
        });
      }
    
  }


