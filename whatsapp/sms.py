import requests
username = "kibongo"
password = ".Kibongo@1141"
phone = "0781478484"
data={
    'recipients':phone,
    'message':'Testing',
    'sender':'Kana'
    }

r=requests.post(
        'https://www.intouchsms.co.rw/api/sendsms/.json',
        data,
        auth=(username,password)
        )
js = r.json();
if js['details'][0]['status'] == 'Q':
    print("Done")

# print (js['details'][0]['status'], r.status_code)