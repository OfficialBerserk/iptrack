import datetime
import os
import sys
import requests
import json

def iptrack():
    # import datetime
    # import requests
    # import json
    # import os
    ip_addr = input("Enter valid IP address to Track: ")
    req01 = requests.get(f"http://ipinfo.io/{ip_addr}")
    req2 = requests.get(f"http://ip-api.com/json/{ip_addr}")
    req3 = requests.get(f"http://api.db-ip.com/v2/free/{ip_addr}")
    resp01 = json.loads(req01.text)
    resp2 = json.loads(req2.text)
    resp3 = json.loads(req3.text)
    #full_ip_data = resp01 + resp2 + resp3
    ipinforesults1 = json.dumps(resp01, indent=2)
    ipinforesults2 = json.dumps(resp2, indent=2)
    ipinforesults3 = json.dumps(resp3, indent=2)
    #datetime = print(datetime.datetime.now())
    print(f"""
IP address Information>
Date/time Recorded at: {datetime.datetime.now()}
{ipinforesults1}
{ipinforesults3}
{ipinforesults2}
""")

iptrack()