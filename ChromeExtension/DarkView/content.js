function invertDivColors() {
  const divs = document.querySelectorAll('div');
  
  divs.forEach(div => {
    div.style.backgroundColor = 'black';
    div.style.color = 'white';
    div.style.fontWeight = 'bold';
  });
}

function revertDivColors() {
  const divs = document.querySelectorAll('div');
  
  divs.forEach(div => {
    div.style.backgroundColor = '';
    div.style.color = '';
    div.style.fontWeight = '';
  });
}

chrome.storage.local.get(['inverted'], function(result) {
  if (result.inverted) {
    invertDivColors();
  }
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'toggle') {
    chrome.storage.local.get(['inverted'], function(result) {
      if (result.inverted) {
        revertDivColors();
        chrome.storage.local.set({ inverted: false });
      } else {
        invertDivColors();
        chrome.storage.local.set({ inverted: true });
      }
      sendResponse({ status: 'done' });
    });
  }
});
