import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ExplanationResponse } from '../../models/explanation.model';
import { marked } from 'marked';

@Component({
  selector: 'app-explanation-view',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './explanation-view.component.html',
  styleUrls: ['./explanation-view.component.css']
})
export class ExplanationViewComponent {
  @Input() explanation!: ExplanationResponse;
  activeTab: 'summary' | 'detailed' | 'concepts' = 'summary';

  formatReadTime(minutes: number): string {
    return `${minutes} min read`;
  }

  renderMarkdown(content: string): string {
    return marked(content) as string;
  }

  getDifficultyClass(difficulty: string): string {
    const classes: { [key: string]: string } = {
      'beginner': 'bg-green-100 text-green-800',
      'intermediate': 'bg-yellow-100 text-yellow-800',
      'advanced': 'bg-red-100 text-red-800'
    };
    return classes[difficulty] || 'bg-gray-100 text-gray-800';
  }
}
