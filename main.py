import requests
import json
import time
import threading
import os
import random
from platform import system

def parse_raw_cookie(raw_cookie_string):
    cookies = {}
    parts = raw_cookie_string.strip().split(';')
    for item in parts:
        if '=' in item:
            k, v = item.strip().split('=', 1)
            cookies[k.strip()] = v.strip()
    return cookies

# 1. Read cookies from cookies.txt (browser se copy kari string paste karni hai)
with open('cookies.txt', 'r') as f:
    raw_cookie = f.read().strip()
cookies = parse_raw_cookie(raw_cookie)

# 2. Aapki main script logic yahan shuru karo
def send_messages():
    # Example file reading (baaki logic aapka original jaise ho)
    with open('FL.txt') as f:
        fl_file = f.read().strip()
    with open(fl_file) as f:
        messages = [msg.strip() for msg in f if msg.strip()]

    # Example: Facebook API/endpoint URL (yahan apne logic ke mutabik daalna hoga)
    url = "https://facebook.com/messages/send"  # apna endpoint
    headers = {
        "User-Agent": "Mozilla/5.0"
        # Baaki headers agar chahiye
    }
    for msg in messages:
        payload = {
            "message": msg
            # Baaki params jo chahiye
        }
        # Cookie dict pass karo
        resp = requests.post(url, data=payload, headers=headers, cookies=cookies)
        print(resp.status_code, resp.text)
        time.sleep(2)  # Delay optional

# Main call yahan se
if __name__ == "__main__":
    send_messages()
