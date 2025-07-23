document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('toggleBtn');
  
  chrome.storage.local.get(['inverted'], function(result) {
    if (result.inverted) {
      toggleBtn.textContent = 'Revert Colors';
    } else {
      toggleBtn.textContent = 'Invert Colors';
    }
  });

  toggleBtn.addEventListener('click', () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, { action: 'toggle' }, function(response) {
        chrome.storage.local.get(['inverted'], function(result) {
          if (result.inverted) {
            toggleBtn.textContent = 'Revert Colors';
          } else {
            toggleBtn.textContent = 'Invert Colors';
          }
        });
      });
    });
  });
});
