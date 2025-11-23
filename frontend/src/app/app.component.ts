import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './components/header/header.component';
import { ExplainFormComponent } from './components/explain-form/explain-form.component';
import { ExplanationViewComponent } from './components/explanation-view/explanation-view.component';
import { ExplanationResponse } from './models/explanation.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    HeaderComponent,
    ExplainFormComponent,
    ExplanationViewComponent
  ],
  template: `
    <main class="min-h-screen">
      <app-header></app-header>

      <div class="container mx-auto px-4 py-8 max-w-6xl">
        <!-- Hero Section -->
        <div class="text-center mb-12">
          <h1 class="text-5xl font-bold mb-4 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            AI Content Explainer
          </h1>
          <p class="text-xl text-gray-600 mb-2">
            Understand technical content at any level
          </p>
          <p class="text-gray-500">
            From "Explain Like I'm 5" to expert-level analysis
          </p>
        </div>

        <!-- Main Content -->
        <div class="grid gap-8">
          <!-- Input Form -->
          <app-explain-form
            (explanationGenerated)="onExplanationGenerated($event)"
            (loadingChange)="onLoadingChange($event)">
          </app-explain-form>

          <!-- Loading State -->
          <div *ngIf="loading" class="flex items-center justify-center py-12">
            <div class="text-center">
              <div class="spinner rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
              <p class="text-gray-600">Generating explanation...</p>
            </div>
          </div>

          <!-- Explanation Result -->
          <app-explanation-view
            *ngIf="explanation && !loading"
            [explanation]="explanation">
          </app-explanation-view>
        </div>

        <!-- Features Section -->
        <div *ngIf="!explanation && !loading" class="mt-16 grid md:grid-cols-3 gap-6">
          <div class="bg-white rounded-lg p-6 shadow-md hover:shadow-lg transition-shadow">
            <div class="text-4xl mb-3">🎯</div>
            <h3 class="text-lg font-semibold mb-2">Multi-Level Explanations</h3>
            <p class="text-gray-600 text-sm">From ELI5 to expert level - choose your complexity</p>
          </div>

          <div class="bg-white rounded-lg p-6 shadow-md hover:shadow-lg transition-shadow">
            <div class="text-4xl mb-3">📚</div>
            <h3 class="text-lg font-semibold mb-2">Multiple Sources</h3>
            <p class="text-gray-600 text-sm">Articles, GitHub repos, PDFs, and more</p>
          </div>

          <div class="bg-white rounded-lg p-6 shadow-md hover:shadow-lg transition-shadow">
            <div class="text-4xl mb-3">💡</div>
            <h3 class="text-lg font-semibold mb-2">Interactive Learning</h3>
            <p class="text-gray-600 text-sm">Ask follow-up questions and dive deeper</p>
          </div>
        </div>
      </div>
    </main>
  `
})
export class AppComponent {
  explanation: ExplanationResponse | null = null;
  loading = false;

  onExplanationGenerated(explanation: ExplanationResponse) {
    this.explanation = explanation;
  }

  onLoadingChange(loading: boolean) {
    this.loading = loading;
  }
}
