const API_URL = 'http://localhost:8000';

// Get current tab URL
async function getCurrentTab() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  return tab;
}

// Display current URL
getCurrentTab().then(tab => {
  const urlDisplay = document.getElementById('current-url');
  urlDisplay.textContent = `📄 ${tab.title || tab.url}`;
});

// Handle explain button click
document.getElementById('explain-btn').addEventListener('click', async () => {
  const level = document.getElementById('level').value;
  const mode = document.getElementById('mode').value;
  const explainBtn = document.getElementById('explain-btn');
  const loading = document.getElementById('loading');
  const result = document.getElementById('result');
  const errorDiv = document.getElementById('error');

  // Reset UI
  explainBtn.disabled = true;
  loading.style.display = 'block';
  result.style.display = 'none';
  errorDiv.style.display = 'none';

  try {
    // Get current page URL
    const tab = await getCurrentTab();
    const url = tab.url;

    // Make API request
    const response = await fetch(`${API_URL}/api/v1/explanation/explain`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        url: url,
        level: level,
        mode: mode,
        generate_visuals: false,
        include_examples: true,
        include_prerequisites: true,
      }),
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }

    const explanation = await response.json();

    // Display results
    document.getElementById('result-badge').textContent =
      `${level.toUpperCase()} • ${mode}`;
    document.getElementById('summary').textContent = explanation.summary;

    // Display takeaways
    const takeawaysDiv = document.getElementById('takeaways');
    takeawaysDiv.innerHTML = '';
    explanation.key_takeaways.forEach(takeaway => {
      const div = document.createElement('div');
      div.className = 'takeaway';
      div.textContent = takeaway;
      takeawaysDiv.appendChild(div);
    });

    // Store full explanation for later
    chrome.storage.local.set({ lastExplanation: explanation });

    result.style.display = 'block';

  } catch (error) {
    console.error('Error:', error);
    errorDiv.textContent = `Failed to generate explanation: ${error.message}. Make sure the API is running.`;
    errorDiv.style.display = 'block';
  } finally {
    loading.style.display = 'none';
    explainBtn.disabled = false;
  }
});

// Handle view full button
document.getElementById('view-full').addEventListener('click', () => {
  chrome.storage.local.get('lastExplanation', (data) => {
    if (data.lastExplanation) {
      // Open web app with explanation
      const webAppUrl = 'http://localhost:3000';
      chrome.tabs.create({ url: webAppUrl });
    }
  });
});
