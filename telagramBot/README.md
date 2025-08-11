# 🤖 Multi-Feature Telegram Bot

## 📌 Overview
This is a **Python-based Telegram Bot** designed for **normal conversations** and **fun, utility-packed features**.  
From Wikipedia searches to math tables, emoji generation to COVID-19 stats — this bot is your **all-in-one assistant** on Telegram.  

## ✨ Features
The bot supports these commands and features:

### 📚 Information & Utilities
- **`wiki <topic>`** → Search Wikipedia and get a short summary.  
  Example: `wiki tajmahal`
- **`big <text>`** → Convert text into ASCII art using `pyfiglet`.
- **`emoji <word>`** → Convert a word into its emoji representation.  
  Example: `emoji smile`
- **`word in <number>`** → Convert numbers into words.  
  Example: `word in 12` → Twelve
- **`url <link>`** → Shorten URLs using TinyURL.
- **`table <number>`** → Generate multiplication tables (1–10).
- **`insta <username>`** → Fetch Instagram profile details (followers, bio, profile pic link, etc.).
- **`trans <text>`** → Translate English text to Hindi.
- **`rev <text>`** → Reverse the text.
- **`cap <text>`** → Convert text to uppercase.
- **`small <text>`** → Convert text to lowercase.
- **`calc <expression>`** → Simple calculator to evaluate expressions.  
  Example: `calc 12+5*3`

### 🦠 COVID-19 Stats
- **`covid world`** → Get global COVID-19 stats.  
- **`covid <country>`** → Get COVID-19 stats for a specific country.

### 🎵 Media & Fun
- **`ytplay <topic>`** → Play a YouTube video directly.
- **`find <topic>`** → Search on Google.
- **`bitcoin`** → Get the current Bitcoin price in USD.
- **`month <month> <year>`** → Show a calendar for a given month and year.  
  Example: `month 9 1997`

## 🛠️ Tech Stack
- **Python 3**
- **Telegram Bot API**
- Libraries:  
  `wikipedia`, `textblob`, `pyfiglet`, `emojis`, `pyshorteners`, `instaloader`, `translate`, `covid`, `pywhatkit`, `cryptocompare`, `calendar`

