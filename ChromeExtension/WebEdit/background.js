chrome.commands.onCommand.addListener((command) => {
    if (command === "toggle-design-mode") {
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
          target: { tabId: tabs[0].id },
          function: toggleDesignMode
        });
      });
    }
  });
  
  function toggleDesignMode() {
    if (document.designMode === 'off') {
      document.designMode = 'on';
    } else {
      document.designMode = 'off';
    }
  }
  