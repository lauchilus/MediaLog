import { Component } from '@angular/core';
import { TuiAvatarComponent, TuiAvatarModule, tuiAvatarOptionsProvider } from '@taiga-ui/kit';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [TuiAvatarModule],
  providers: [tuiAvatarOptionsProvider({
    size: 'l',
    autoColor: true,
    rounded: true,
}),TuiAvatarComponent],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {

}
