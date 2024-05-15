import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { SearchMediaComponent } from './components/page/search-media/search-media.component';

export const routes: Routes = [

    { path: 'home', component: HomeComponent },
    { path: 'search/:type', component: SearchMediaComponent },



    { path: '**', redirectTo: '/home', pathMatch: 'full' }
];
