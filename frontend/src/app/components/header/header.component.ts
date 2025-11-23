import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule],
  template: `
    <header class="border-b bg-white shadow-sm">
      <div class="container mx-auto px-4 py-4 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="text-2xl">🧠</span>
          <span class="font-bold text-xl">AI Content Explainer</span>
        </div>

        <nav class="flex items-center gap-6">
          <a href="#" class="text-gray-600 hover:text-gray-900 transition-colors">
            Features
          </a>
          <a href="#" class="text-gray-600 hover:text-gray-900 transition-colors">
            Pricing
          </a>
          <button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">
            Get Started
          </button>
        </nav>
      </div>
    </header>
  `
})
export class HeaderComponent {}
