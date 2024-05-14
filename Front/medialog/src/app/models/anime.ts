export interface Anime {
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
