import pywebview

async def capture_screenshot():
  # Send message to content script to capture screenshot
  await pywebview.evaluate_javascript("""
  window.chrome.tabs.sendMessage(window.chrome.tabs.query({active: True})[0].id, {"action": "capture"})
  """)

button = pywebview.api.get_button("captureBtn")  # Access button using pywebview API
button.clicked_event += capture_screenshot  # Add click event listener
