import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Classement } from '../models/classement.model';

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  private apiBaseUrl = 'https://f1-dashboard-backend-cm01.onrender.com'; // ← remplacer par ton URL

  constructor(private http: HttpClient) {}

  /**
   * Récupère le classement selon le filtre et la saison
   * @param by - filtre principal (ex: driver, constructor)
   * @param season - année ou saison
   */
  getClassement(by: string, season: number): Observable<Classement[]> {
    let params = new HttpParams()
      .set('by', by)
      .set('season', season);

    return this.http.get(`${this.apiBaseUrl}/classement`, { params }) as Observable<Classement[]>;
  }
}
