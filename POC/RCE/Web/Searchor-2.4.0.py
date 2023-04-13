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

    data = f'POC is not to be shared unless HTB:Busqueda is live for 7 days'

    response = requests.post(f'{victim_url}', headers=headers, data=data)

try:
    main()
except:
    print(f"""
    Usage:
        {sys.argv[0]} victim_url attacker_ip attacker_port
    """)
