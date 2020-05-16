import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { HomeComponent } from './components/home/home.component';
import { ProfileSidebarComponent } from './components/home/profile-sidebar/profile-sidebar.component';
import { TimelineComponent } from './components/home/timeline/timeline.component';


const routes: Routes = [
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'home', component: HomeComponent },
  { path: 'profile-sidebar', component: ProfileSidebarComponent },
  { path: 'timeline', component: TimelineComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

// An array of routing components so that it doesn't need to be decleared again in app.module.ts 
export const RoutingComponents = [LoginComponent, RegisterComponent, HomeComponent, 
  ProfileSidebarComponent, TimelineComponent ]
