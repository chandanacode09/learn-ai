// Content script - runs on web pages

// This could be extended to add features like:
// - Right-click context menu to explain selected text
// - Inline explanations
// - Highlighting key concepts on the page

console.log('AI Content Explainer extension loaded');

// Example: Listen for text selection
document.addEventListener('mouseup', () => {
  const selectedText = window.getSelection().toString().trim();
  if (selectedText.length > 50) {
    // Could show a tooltip or button to explain the selected text
    // For MVP, we'll keep it simple
  }
});
