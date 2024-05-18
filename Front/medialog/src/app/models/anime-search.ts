export interface AnimeSearch {id: number
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