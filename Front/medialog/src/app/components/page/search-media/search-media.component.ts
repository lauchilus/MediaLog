import { Component, Input, input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
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
import { Anime } from '../../../models/anime';

@Component({
  selector: 'app-search-media',
  standalone: true,
  imports: [DescriptionPipe, RouterModule],
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
  animePaging = {
    next : '',
    prev : ''
  };

  selectedContent: any | null = null;
  search: string = '';
  page: number = 1;

  constructor(private bookService: BooksService, private movieService: MoviesService, private animeService: AnimeService, private serieService: SeriesService, private gamesService: GamesService, private activatedRoute: ActivatedRoute, private router: Router) { }


  ngOnInit(): void {
    this.activatedRoute.paramMap.subscribe(params => {
      var t = params.get('type')!;
      if (t !== this.title) {
        this.title = t;
      }

    });

    this.activatedRoute.queryParamMap.subscribe(params => {
      this.search = params.get('q') || '';
      this.page = +params.get('page')!;
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
        } else {
          this.bookService.GetBooksList(this.page).subscribe(
            (data) => {
              this.content = {
                pagination: {
                  page: this.page,
                  total_pages: 100,
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
          this.movieService.GetMoviesList(this.page).subscribe(
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
          this.serieService.GetSeriesList(this.page).subscribe(
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
        if (this.search.length !== 0) {
          this.animeService.GetAnimeSearch(this.search).subscribe(
            (res: any) => {
              this.content = {
                pagination: {
                  page: this.page,
                  total_pages: 1,
                  total_results: 0
                },
                items: res.data as Anime[],


              },
                this.animePaging = {
                  next: res.paging.next ? res.paging.next : '' ,
                  prev: res.paging.previous ? res.paging.previous : '' ,
                },
                console.log(res.paging)

            });

        } else {
          this.animeService.GetAnimeList().subscribe(
            (data) => {

              this.content = {
                pagination: {
                  page: this.page,
                  total_pages: 100,
                  total_results: 0
                },
                items: data.data as Anime[]
              },
              this.animePaging = {
                next: data.paging.next ? data.paging.next : ''  ,
                prev: data.paging.previous ? data.paging.previous : '' ,
              },
              console.log(data.paging)

            });
        }
        break;
      case 'Games':
        if (this.search.length !== 0) {
          this.gamesService.GetGamesSearch(this.search, this.page).subscribe(
            (res: any) => {
              this.content = {
                pagination: {
                  page: this.page,
                  total_pages: 100,
                  total_results: 1000
                },
                items: res as Movie[]
              }

            });
        } else {
          this.gamesService.GetGamesList(this.page).subscribe(
            (data) => {
              this.content = {
                pagination: {
                  page: this.page,
                  total_pages: 100,
                  total_results: 1000
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

  PrevPage() {
    if (this.title === "Animes") {
      this.ChangePageAnime(this.animePaging.prev)
    } else {
      this.page--;
      this.NavigateSearch()
    }
  }

  NextPage() {
    if (this.title === "Animes") {
      this.ChangePageAnime(this.animePaging.next)
    } else {
      this.page = this.addWithLimit(this.page,1,this.content.pagination.total_pages+1);
      this.NavigateSearch()
    }
  }

  private ChangePageAnime(url: string){
    this.animeService.ChangePage(url).subscribe(
      (res: any) => {
        this.content = {
          pagination: {
            page: this.page,
            total_pages: this.page+1,
            total_results: 0
          },
          items: res.data as Anime[],


        },
          this.animePaging = {
            next: res.paging.next ? res.paging.next : ''  ,
            prev: res.paging.previous? res.paging.previous : '' ,
          },
          console.log(res.paging)

      });
      
  }

  private addWithLimit(currentValue: number, increment: number, maxValue: number): number {
    const newValue = currentValue + increment;
    return newValue >= maxValue ? maxValue : newValue;
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

export interface SearchAnime {
  items: Anime[]
  pagination: Paging
}

export interface Daum {
  node: Node
  ranking: Ranking
}

export interface Node {
  id: number
  title: string
  main_picture: MainPicture
}

export interface MainPicture {
  medium: string
  large: string
}

export interface Ranking {
  rank: number
}

export interface Paging {
  next: string
  prev: string
}
