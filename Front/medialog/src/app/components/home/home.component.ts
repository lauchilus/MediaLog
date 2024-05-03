import { Component, OnInit } from '@angular/core';
import { BooksService } from '../../services/books.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit{
  books: any[] = [];

  constructor(private bookService: BooksService) { }

  ngOnInit(): void {
    this.getItems();
    
  }

  getItems(): void {
    this.bookService.GetBooksList().subscribe(
      (data) => {
        this.books = data.map((book: any) =>{
          return{
            ...book,
            
          }          
        });console.log(this.books)
      },
      error =>{
        console.log(error);
      }
    )
  }
}

