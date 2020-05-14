import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
// RoutingComponent imported - an array of routing components
import { AppRoutingModule, RoutingComponents } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProfileSidebarComponent } from './components/home/profile-sidebar/profile-sidebar.component';



@NgModule({
  declarations: [
    AppComponent,
    RoutingComponents,
    ProfileSidebarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
