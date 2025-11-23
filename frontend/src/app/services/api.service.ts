import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ExplainRequest, ExplanationResponse } from '../models/explanation.model';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000/api/v1';

  constructor(private http: HttpClient) {}

  explainContent(request: ExplainRequest): Observable<ExplanationResponse> {
    return this.http.post<ExplanationResponse>(
      `${this.apiUrl}/explanation/explain`,
      request
    );
  }

  getExample(): Observable<ExplanationResponse> {
    return this.http.get<ExplanationResponse>(
      `${this.apiUrl}/explanation/example`
    );
  }

  healthCheck(): Observable<{ status: string }> {
    return this.http.get<{ status: string }>(`${this.apiUrl}/health`);
  }
}
