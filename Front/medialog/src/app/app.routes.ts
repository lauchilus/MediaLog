import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { SearchMediaComponent } from './components/page/search-media/search-media.component';
import { DetailsComponent } from './components/details/details.component';

export const routes: Routes = [

    { path: 'home', component: HomeComponent },
    { path: 'search/:type', component: SearchMediaComponent },
    { path: 'details/:type/:id', component: DetailsComponent},



    { path: '**', redirectTo: '/home', pathMatch: 'full' }
];
