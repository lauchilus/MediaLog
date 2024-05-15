import { Component, Input, input, OnInit } from '@angular/core';
import { DescriptionPipe } from '../../../pipes/description.pipe';
import { AnimeService } from '../../../services/anime.service';
import { BooksService } from '../../../services/books.service';
import { GamesService } from '../../../services/games.service';
import { MoviesService } from '../../../services/movies.service';
import { SeriesService } from '../../../services/series.service';
import { IBook } from '../../../models/book';
import { animate, style, transition, trigger } from '@angular/animations';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { Movie } from '../../../models/movie';

@Component({
  selector: 'app-search-media',
  standalone: true,
  imports: [DescriptionPipe,RouterModule],
  templateUrl: './search-media.component.html',
  styleUrl: './search-media.component.css',
  animations: [
    trigger('fade', [
      transition('void => *', [
        style({ opacity: 0 }),
        animate(300, style({ opacity: 1 }))
      ])
    ])
  ]
})
export class SearchMediaComponent implements OnInit {

  title!: string;

  content!: SearchItems;
  selectedContent: any | null = null;
  search: string = '';
  page !: number;

  constructor(private bookService: BooksService, private movieService: MoviesService, private animeService: AnimeService, private serieService: SeriesService, private gamesService: GamesService, private activatedRoute: ActivatedRoute, private router: Router) { }

  ngOnInit(): void {
    this.activatedRoute.paramMap.subscribe(params => {
      this.title = params.get('type')!;
      this.SearchMedia();
    });

    this.activatedRoute.queryParamMap.subscribe(params => {
      this.search = params.get('q') || '';
      this.page = +params.get('page')! || 1;
      this.SearchMedia();
    });

  }

  NavigateSearch() {

    this.router.navigate(['/search', this.title], {
      queryParams: {
        q: this.search,
        page: this.page
      },
      queryParamsHandling: 'merge'
    });
  }

  SearchMedia() {
    switch (this.title) {
      case 'Books':
        if (this.search.length !== 0) {
        this.bookService.GetBooksSearch(this.search, this.page).subscribe(
          (res: any) => {
            this.content = {
              pagination: res.pagination,
              items: res.books as IBook[]

            }, console.log(this.content)

          });
        }else{
          this.bookService.GetBooksList().subscribe(
            (data) => {
              this.content = {
                pagination: {
                  page: 0,
                  total_pages: 0,
                  total_results: 0
                },
                items: data as IBook[]
                
              }     
              });
        }
        break;
      case 'Movies':
        if (this.search.length !== 0) {
          this.movieService.GetMoviesSearch(this.search, this.page).subscribe(
            (res: any) => {
              this.content = {
                pagination: res.pagination,
                items: res.movies as Movie[]

              }

            });
        } else {
          this.movieService.GetMoviesList().subscribe(
            (data) => {
              this.content = {
                pagination: data.pagination,
                items: data.movies as Movie[]
              }
            });
        }

        break;
      case 'Series':
        if (this.search.length !== 0) {
          this.serieService.GetSeriesSearch(this.search, this.page).subscribe(
            (res: any) => {
              this.content = {
                pagination: res.pagination,
                items: res.movies as Movie[]

              }

            });
        } else {
          this.serieService.GetSeriesList().subscribe(
            (data) => {
              this.content = {
                pagination: data.pagination,
                items: data.movies as Movie[]
              }
            });
        }
        break;
      case 'Animes':
        // TODO: ADD ANIME AN PAGINATION LOGIC
        break;
      case 'Games':
        if (this.search.length !== 0) {
          this.gamesService.GetGamesSearch(this.search, this.page).subscribe(
            (res: any) => {
              this.content = {
                pagination: {
                  page: 0,
                  total_pages: 0,
                  total_results: 0
                },
                items: res as Movie[]

              }

            });
        } else {
          this.gamesService.GetGamesList().subscribe(
            (data) => {
              this.content = {
                pagination: {
                  page: 0,
                  total_pages: 0,
                  total_results: 0
                },
                items: data as Movie[]
              },
              console.log(this.content)
            });
        }
        break;
      default:
        console.log("aa")
        break;
    }
  }


  setHoverElement(element: any) {
    this.selectedContent = element.id ?? element.node.title;
  }

  clearHoverElement() {
    this.selectedContent = null;
  }

  onInputChange(event: any) {
    let input = event.target.value
    this.search = input;
  }

}

export interface SearchItems {
  pagination: Pagination
  items: any[]
}

export interface Pagination {
  page: number
  total_pages: number
  total_results: number
}

function get(arg0: string) {
  throw new Error('Function not implemented.');
}
