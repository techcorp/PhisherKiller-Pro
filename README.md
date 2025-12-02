# PHISHERKILLER PRO 2025

### The Ultimate AI‑Powered Phishing & Malware URL Scanner

<p align="center">
  <img src="https://github.com/techcorp/PhisherKiller-Pro/blob/530ebe28133e10284e02e8b1a61052f0d3965988/PhisherKiller.png" alt="PhishKiller Banner">

[![License:
MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python
3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![VirusTotal](https://img.shields.io/badge/VirusTotal-Integrated-red)](https://virustotal.com)
[![Gemini
AI](https://img.shields.io/badge/Gemini%20AI-Powered-green)](https://ai.google.dev)
</p>
<br>
------------------------------------------------------------------------

## Features

| Feature | Description |
|--------|-------------|
| **Real VirusTotal Scan** | Checks URL with 90+ antivirus engines |
| **Gemini AI Explanation** | Explains how the phishing attack works |
| **Smart Danger Score (0–100)** | Calculates risk using domain, content analysis and VT hits |
| **Animated Progress Bar** | Smooth scanning animation |
| **Permanent Banner** | Professional look every time |
| **Menu System** | Scan • View Reports • Exit |
| **PDF + TXT Reports** | Auto-saves reports with AI verdict |
| **Works Offline** | Only APIs require internet |
| **Runs Everywhere** | Windows • Linux • Termux |


------------------------------------------------------------------------

## Installation & Setup

### 1. Install Python

Windows: Install from python.org\
Linux/Termux: Usually preinstalled

### 2. Clone the Repository

``` bash
git clone https://github.com/techcorp/PhisherKiller-Pro.git
cd PhisherKiller-Pro
```

### 3. Install Requirements

``` bash
pip install requests colorama beautifulsoup4 reportlab
```

### 4. Get API Keys

**VirusTotal**\
Signup → Profile → API Key\
Free: 500 scans/day
<br>
<br>
<p align="center">
  <img src="How to Get VirusTotal API Key.png" alt="Virus Total API Key">
</p>
<br>
<br>

**Google Gemini**\
https://aistudio.google.com/app/apikey\
Free: 1500 requests/day
<br>
<br>
<p align="center">
  <img src="How to get Gemini API Keys.png" alt="Gemini API Key">
</p>

------------------------------------------------------------------------

### 5. Add Keys to Code

In `phisherkiller.py`:

``` python
GEMINI_API_KEY = "your_gemini_api_key_here"
VT_API_KEY     = "your_virustotal_api_key_here"
```

Example:

``` python
GEMINI_API_KEY = "AIzaSyDxxxxxxxxxxxxxxxxxxxxxxxx"
VT_API_KEY = "64d5e2f1a2b3c4d5e6f7g8h9i0..."
```

------------------------------------------------------------------------

### 6. Run the Tool

``` bash
python phisherkiller.py
```

### Sample Output

    DANGER LEVEL: 94/100  
    VT STATUS: DETECTED (11 engines)

    This is a confirmed phishing page.  
    They want your email and password to hack your account.  
    Report saved as PDF + TXT.

------------------------------------------------------------------------

## Termux (Android)

``` bash
pkg install python
pip install requests colorama beautifulsoup4 reportlab
git clone https://github.com/techcorp/PhisherKiller-Pro.git
cd PhisherKiller-Pro
python phisherkiller.py
```

------------------------------------------------------------------------

## Disclaimer

Educational and defensive security use only.\
Do not misuse.

------------------------------------------------------------------------

## Author

**Technical Corp**\
GitHub: github.com/techcorp/
YouTube: [Technical Corp](https://www.youtube.com/@technicalcorp)
