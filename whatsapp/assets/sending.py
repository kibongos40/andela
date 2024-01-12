import requests
import time

filename = 'c:/xampp/htdocs/andela/whatsapp/assets/numbers.txt'
start_line = 751

with open(filename, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if line_number < start_line:
            continue
        # 'enumerate' starts counting from 1 by default
        # print(f"Line {line_number}: {line.strip()}")
        phone = line.strip()

        username = "kibongo"
        password = ".Kibongo@1141"
        message = "Join us from 7pm to 11pm at Kana Cocktails and snacks (KBC building floor C2) and enjoy the best karaoke night with your vocalist Andrew kats alongside other great singers. DON'T MISS Tel:0785237787"
        data={
            'recipients':phone,
            'message':message,
            'sender':'Kana'
            }

        r=requests.post(
                'https://www.intouchsms.co.rw/api/sendsms/.json',
                data,
                auth=(username,password)
                )
        js = r.json();

        if js['details'][0]['status'] == 'Q':
            print(phone, line_number,"Done")