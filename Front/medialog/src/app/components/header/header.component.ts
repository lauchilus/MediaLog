import { trigger, state, style, transition, animate } from '@angular/animations';
import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { RouterModule } from '@angular/router';
import { TuiAvatarComponent, TuiAvatarModule, tuiAvatarOptionsProvider } from '@taiga-ui/kit';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [TuiAvatarModule, RouterModule],
  providers: [tuiAvatarOptionsProvider({
    size: 'l',
    autoColor: true,
    rounded: true,
  }), TuiAvatarComponent],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css',
  animations: [
    trigger("openClose", [
      // ...
      state(
        "open",
        style({
          opacity: 1,
          transform: "scale(1, 1)"
        })
      ),
      state(
        "closed",
        style({
          opacity: 0,
          transform: "scale(0.95, 0.95)"
        })
      ),
      transition("open => closed", [animate("100ms ease-in")]),
      transition("closed => open", [animate("200ms ease-out")])
    ])
  ]
})
export class HeaderComponent implements OnInit {

  @ViewChild('hamMenu') hamMenu!: ElementRef;
  @ViewChild('sidebar') sidebar!: ElementRef;

  toggleMenu: boolean = false

  
  get openCloseTrigger() {
    return this.toggleMenu ? "open" : "closed";
  }

  ngOnInit(): void {

  }
  queryParams = {
    q: '',
    page: 1
  }

  routes = [
    {
      path: '/#',
      label: 'Home'
    },
    {
      path: `/search/Movies`,
      label: 'Movies'
    },
    {
      path: '/search/Series',
      label: 'Series'
    },
    {
      path: '/search/Animes',
      label: 'Animes'
    },
    {
      path: '/search/Games',
      label: 'Games'
    },
    {
      path: '/search/Books',
      label: 'Books'
    },
  ]

  ToggleMenu() {
    this.toggleMenu = !this.toggleMenu;

    if (this.toggleMenu) {
      this.sidebar.nativeElement.style.display = 'flex';
      this.hamMenu.nativeElement.style.display = 'none'
    } else {
      this.sidebar.nativeElement.style.display = 'none';
      this.hamMenu.nativeElement.style.display = 'flex'
    }
  }

}


