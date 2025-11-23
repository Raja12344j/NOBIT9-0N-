import requests
import time

def parse_raw_cookie(raw_cookie_string):
    cookies = {}
    parts = raw_cookie_string.strip().split(';')
    for item in parts:
        if '=' in item:
            k, v = item.strip().split('=', 1)
            cookies[k.strip()] = v.strip()
    return cookies

# 1. Read cookies from cookies.txt
with open('cookies.txt', 'r') as f:
    raw_cookie = f.read().strip()
cookies = parse_raw_cookie(raw_cookie)

# 2. Read msg file name from FL.txt, then get messages
with open('FL.txt') as f:
    message_file = f.read().strip()

with open(message_file) as f:
    messages = [msg.strip() for msg in f if msg.strip()]

# 3. Replace with your actual Facebook API/message endpoint and payload format!
url = "https://facebook.com/messages/send"   # <-- Change this as per your actual use
headers = {
    "User-Agent": "Mozilla/5.0"
}

for msg in messages:
    payload = {
        "message": msg,
        "recipient_id": "100058845120522"  # ID ya jo field aapke use-case me ho
    }
    response = requests.post(url, data=payload, headers=headers, cookies=cookies)
    print(response.status_code, response.text)
    time.sleep(2)  # optional delay
