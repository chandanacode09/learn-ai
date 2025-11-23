import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import {
  ExplanationLevel,
  ExplanationMode,
  ExplanationResponse,
  ExplainRequest
} from '../../models/explanation.model';

@Component({
  selector: 'app-explain-form',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './explain-form.component.html',
  styleUrls: ['./explain-form.component.css']
})
export class ExplainFormComponent {
  @Output() explanationGenerated = new EventEmitter<ExplanationResponse>();
  @Output() loadingChange = new EventEmitter<boolean>();

  inputType: 'url' | 'text' | 'github' = 'url';
  url = '';
  text = '';
  githubRepo = '';
  level = ExplanationLevel.INTERMEDIATE;
  mode = ExplanationMode.PERSONAL;
  error = '';

  // Enums for template
  ExplanationLevel = ExplanationLevel;
  ExplanationMode = ExplanationMode;

  constructor(private apiService: ApiService) {}

  onSubmit() {
    this.error = '';
    this.loadingChange.emit(true);

    const request: ExplainRequest = {
      level: this.level,
      mode: this.mode,
      generate_visuals: true,
      include_examples: true,
      include_prerequisites: true
    };

    if (this.inputType === 'url') {
      if (!this.url) {
        this.error = 'Please enter a URL';
        this.loadingChange.emit(false);
        return;
      }
      request.url = this.url;
    } else if (this.inputType === 'text') {
      if (!this.text) {
        this.error = 'Please enter some text';
        this.loadingChange.emit(false);
        return;
      }
      request.content = this.text;
    } else if (this.inputType === 'github') {
      if (!this.githubRepo) {
        this.error = 'Please enter a GitHub repository';
        this.loadingChange.emit(false);
        return;
      }
      request.github_repo = this.githubRepo;
    }

    this.apiService.explainContent(request).subscribe({
      next: (explanation) => {
        this.explanationGenerated.emit(explanation);
        this.loadingChange.emit(false);
      },
      error: (err) => {
        this.error = err.error?.detail || 'Failed to generate explanation';
        console.error(err);
        this.loadingChange.emit(false);
      }
    });
  }

  tryExample() {
    this.error = '';
    this.loadingChange.emit(true);

    this.apiService.getExample().subscribe({
      next: (explanation) => {
        this.explanationGenerated.emit(explanation);
        this.loadingChange.emit(false);
      },
      error: (err) => {
        this.error = err.error?.detail || 'Failed to load example';
        this.loadingChange.emit(false);
      }
    });
  }
}
