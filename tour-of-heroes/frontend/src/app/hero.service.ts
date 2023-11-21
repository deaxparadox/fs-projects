import { Injectable } from '@angular/core';
import { Hero } from './hero';
import { HEROES } from './mock-heroes';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HeroService {

  
  constructor(
    private messageService: MessageService,
    private http: HttpClient,
  ) { }

  private herosUrl = "api/heroes";
  private djangoUrls = "http://localhost:8000/api/v1/heroes/"
  private log(message: string) {
    this.messageService.add(`HeroService: ${message}`);
  }
    
  getHeroes(): Observable<Hero[]> {
    return this.http.get<Hero[]>(this.herosUrl);
  }

  getHero(id: number): Observable<Hero> {
    // For now, assume that a hero with the specified `id` always exists.
    // Error handling will be added in the next step of the tutorial.
    const hero = HEROES.find(h => h.id === id)!;
    this.messageService.add(`HeroService: fetched hero id=${id}`);
    return of(hero);
  }
}
