import requests

url = "https://www.intouchsms.co.rw/api/sendsms/.json"

payload = {
    "sender": "+250781478484",
    "message": "Testing intouch",
    "recipients": "0781478484"
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic a2lib25nbzouS2lib25nb0AxMTQx"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)