export interface IBook {
    id: string
    title: string
    author: Author[]
    publish_date: number
    poster_url: string
  }
  
  export interface Author {
    key: string
    name: string
  }