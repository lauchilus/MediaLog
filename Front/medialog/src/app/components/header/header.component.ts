import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { TuiAvatarComponent, TuiAvatarModule, tuiAvatarOptionsProvider } from '@taiga-ui/kit';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [TuiAvatarModule,RouterModule],
  providers: [tuiAvatarOptionsProvider({
    size: 'l',
    autoColor: true,
    rounded: true,
}),TuiAvatarComponent],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {
  queryParams = {
    q: '',
    page: 1
  }
  routes = [
    {
      path : '/#',
      label: 'Home'
    },
    {
      path : `/search/Movies`,
      label: 'Movies'
    },
    {
      path : '/search/Series',
      label: 'Series'
    },
    {
      path : '/search/Animes',
      label: 'Animes'
    },
    {
      path : '/search/Games',
      label: 'Games'
    },
    {
      path : '/search/Books',
      label: 'Books'
    },
  ]
}
