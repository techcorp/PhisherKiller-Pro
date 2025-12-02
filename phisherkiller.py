# =======================================================
#  PHISHERKILLER PRO 2025
#  Full Menu • VirusTotal • Gemini AI • PDF Report • Banner Forever
# =======================================================

import os
import sys
import time
import requests
from datetime import datetime
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Auto install
os.system("pip install --quiet requests colorama beautifulsoup4 reportlab 2>nul")

from colorama import init, Fore, Style
init(autoreset=True)

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    PDF = True
except:
    PDF = False

# === ADD YOUR API KEYS HERE ===
GEMINI_API_KEY = "your_gemini_api_key_here"          # Get free: https://aistudio.google.com/app/apikey
VT_API_KEY     = "your_virustotal_api_key_here"      # Get free: https://www.virustotal.com/gui/join-us

REPORTS_DIR = "PhishKiller_Reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

# EPIC BANNER (PERMANENT)
print(f"""
{Fore.RED}{Style.BRIGHT}
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
██╔══██╗██║  ██║██║██╔════╝██║  ██║██║  ██║██║██║     ██║     ██╔════╝██╔══██╗
██████╔╝███████║██║███████╗███████║███████║██║██║     ██║     █████╗  ██████╔╝
██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══██║██║██║     ██║     ██╔══╝  ██╔══██╗
██║     ██║  ██║██║███████║██║  ██║██║  ██║██║███████╗███████╗███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
{Fore.CYAN}{Style.BRIGHT}       ULTIMATE AI + VIRUSTOTAL PHISHING KILLER 2025
{Fore.GREEN}         Created by Technical Corp • https://technicalcorpofficial.com
{Fore.YELLOW}        Subscribe to Technical Corp: https://www.youtube.com/@technicalcorp
""")

def progress_bar(i, total=10):
    percent = (i / total) * 100
    filled = int(50 * i // total)
    bar = "█" * filled + "░" * (50 - filled)
    print(f"\r{Fore.CYAN}Scanning [{bar}] {percent:.1f}%", end="", flush=True)

def speak(text):
    if "win" in sys.platform:
        os.system(f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')" >nul 2>&1')
    else:
        os.system(f'termux-tts-speak "{text}" >/dev/null 2>&1')

# All functions (same as before – 100% working)
def vt_scan(url): ...  # (same code as previous version)
def gemini_verdict(url, score, vt_status, vt_hits, title): ...  # (same)
def analyze_page(url): ...  # (same)
def calculate_score(url, data, vt_hits): ...  # (same)
def save_report(url, score, vt_status, vt_hits, engines, data, ai_text): ...  # (same)

# FULL MENU SYSTEM
def main_menu():
    while True:
        print(f"{Fore.CYAN}{'═'*60}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}                   MAIN MENU")
        print(f"{Fore.CYAN}{'═'*60}")
        print(f"{Fore.WHITE}[1] Scan a Suspicious URL")
        print(f"{Fore.WHITE}[2] Open Reports Folder")
        print(f"{Fore.RED}[3] Exit PhisherKiller")
        print(f"{Fore.CYAN}{'═'*60}")
        
        choice = input(f"\n{Fore.YELLOW}Choose option (1-3): {Fore.WHITE}").strip()

        if choice == "1":
            scan_url()
        elif choice == "2":
            os.startfile(REPORTS_DIR) if os.name == 'nt' else os.system(f"xdg-open {REPORTS_DIR}")
            print(f"{Fore.GREEN}Reports folder opened!")
            time.sleep(2)
        elif choice == "3":
            print(f"\n{Fore.RED}{Style.BRIGHT}Shutting down PhisherKiller...")
            speak("Goodbye Cyber Cop")
            print(f"{Fore.GREEN}Stay safe out there. You are the legend!\n")
            sys.exit(0)
        else:
            print(f"{Fore.RED}Invalid option! Try again.")
            time.sleep(1)

def scan_url():
    url = input(f"\n{Fore.CYAN}Enter suspicious URL: {Fore.WHITE}").strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\n{Fore.YELLOW}Launching full scan: {url}\n")
    
    for i in range(1, 11):
        progress_bar(i)
        time.sleep(0.7)
        if i == 3: page_data = analyze_page(url)
        if i == 6: vt_status, vt_hits, vt_engines = vt_scan(url)
        if i == 8: score = calculate_score(url, page_data, vt_hits)
        if i == 9: ai_verdict = gemini_verdict(url, score, vt_status, vt_hits, page_data["title"])
        if i == 10: save_report(url, score, vt_status, vt_hits, vt_engines, page_data, ai_verdict)

    print(f"\n\n{Fore.WHITE}{'═'*70}")
    print(f"{Fore.RED if score >= 70 else Fore.YELLOW}{Style.BRIGHT}DANGER LEVEL: {score}/100 → VT: {vt_status} ({vt_hits} hits)")
    print(f"{Fore.MAGENTA}{ai_verdict}")
    print(f"{Fore.WHITE}{'═'*70}")

    speak("Critical threat detected!" if score >= 70 else "Suspicious link")
    input(f"\n{Fore.CYAN}Press Enter to return to menu...")


def vt_scan(url):
    try:
        r = requests.post("https://www.virustotal.com/api/v3/urls", headers={"x-apikey": VT_API_KEY}, data={"url": url}, timeout=15)
        if r.status_code != 200: return "Error", 0, []
        analysis_id = r.json()["data"]["id"].split("-")[1]
        for _ in range(12):
            time.sleep(5)
            res = requests.get(f"https://www.virustotal.com/api/v3/analyses/{analysis_id}", headers={"x-apikey": VT_API_KEY}, timeout=15)
            data = res.json()
            if data["data"]["attributes"]["status"] == "completed":
                stats = data["data"]["attributes"]["stats"]
                hits = stats["malicious"] + stats["suspicious"]
                engines = [f"{e}: {v['result']}" for e, v in data["data"]["attributes"]["results"].items() if v["category"] in ["malicious","suspicious"]]
                return "DETECTED" if hits > 0 else "CLEAN", hits, engines[:8]
        return "PENDING", 0, []
    except:
        return "OFFLINE", 0, []

def gemini_verdict(url, score, vt_status, vt_hits, title):
    prompt = f"URL: {url}\nScore: {score}/100\nVirusTotal: {vt_status} ({vt_hits} engines)\nTitle: {title}\n\nExplain in scary, simple English with emojis: Is this phishing? What do criminals want? What should victim do NOW?"
    try:
        r = requests.post(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}",
                          json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=25)
        if r.status_code == 200:
            return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except: pass
    return f"GEMINI OFFLINE → VT: {vt_status} ({vt_hits} hits)\nScore {score}/100 = EXTREME DANGER!\nDELETE THIS LINK IMMEDIATELY!"

def analyze_page(url):
    try:
        r = requests.get(url, timeout=12, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"
        pw = len(soup.find_all("input", {"type": "password"}))
        return {"title": title, "pw": pw}
    except:
        return {"title": "Blocked / Timeout", "pw": 0}

def calculate_score(url, data, vt_hits):
    domain = urlparse(url).netloc.lower()
    score = 25
    if any(x in domain for x in ["myfreesites.net","page.tl","000webhost","rf.gd","infinityfree"]): score += 55
    if data["pw"] > 0: score += 40
    if vt_hits > 0: score += min(vt_hits * 10, 50)
    return min(100, score)

def save_report(url, score, vt_status, vt_hits, engines, data, ai_text):
    report = f"""
════════════════════════════════════════════════════════════
              PHISHERKILLER FINAL REPORT
════════════════════════════════════════════════════════════
URL           : {url}
Time          : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
DANGER SCORE  : {score}/100
VIRUSTOTAL    : {vt_status} ({vt_hits} engines)

Detected by:
{chr(10).join(f"→ {e}" for e in engines) if engines else "→ No detections"}

Page Title    : {data['title']}
Password Fields: {data['pw']}

GEMINI AI VERDICT:
{ai_text}

ACTION: DELETE • BLOCK • STAY SAFE
PhisherKiller Pro • Technical Corp
════════════════════════════════════════════════════════════
"""
    txt_file = os.path.join(REPORTS_DIR, f"REPORT_{int(time.time())}.txt")
    with open(txt_file, "w", encoding="utf-8") as f: f.write(report)
    if PDF:
        pdf_file = txt_file.replace(".txt", ".pdf")
        try:
            c = canvas.Canvas(pdf_file, pagesize=letter)
            y = 780
            c.setFont("Helvetica-Bold", 18)
            c.drawCentredString(300, y, "PHISHERKILLER REPORT")
            y -= 50
            c.setFont("Helvetica", 10)
            for line in report.split("\n"):
                if y < 80: c.showPage(); y = 780
                c.drawString(40, y, line[:100])
                y -= 14
            c.save()
            print(f"\n{Fore.GREEN}Report Saved → {pdf_file}")
        except:
            print(f"\n{Fore.GREEN}Report Saved → {txt_file}")
    else:
        print(f"\n{Fore.GREEN}Report Saved → {txt_file}")

# START
speak("PhisherKiller Pro v24 activated")

main_menu()
