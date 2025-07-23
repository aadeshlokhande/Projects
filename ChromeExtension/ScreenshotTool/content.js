chrome.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
    if (message.action === "capture") {
      // Capture screenshot using Chrome extension API
      chrome.tabs.captureVisibleTab(null, async (dataUrl) => {
        // Send captured image data back to popup script
        await window.pywebview.sendMessage({dataUrl: dataUrl})
      })
    }
  });
  