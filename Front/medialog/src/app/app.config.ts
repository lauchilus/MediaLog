import { provideAnimations } from "@angular/platform-browser/animations";
import { TuiRootModule } from "@taiga-ui/core";
import { ApplicationConfig, importProvidersFrom } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { HttpClientModule } from "@angular/common/http";

export const appConfig: ApplicationConfig = {
  providers: [provideAnimations(), provideRouter(routes), importProvidersFrom(TuiRootModule),importProvidersFrom(HttpClientModule),provideAnimations()]
};
