// Background service worker for Chrome extension

// Listen for installation
chrome.runtime.onInstalled.addListener(() => {
  console.log('AI Content Explainer extension installed');
});

// Listen for messages from content scripts
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'explainSelection') {
    // Handle text selection explanation
    handleSelectionExplanation(request.text)
      .then(sendResponse)
      .catch(error => sendResponse({ error: error.message }));
    return true; // Keep message channel open for async response
  }
});

async function handleSelectionExplanation(text) {
  // This could be extended to explain selected text
  return { success: true };
}
