# TODO: To Verify Email through Google Spreadsheet `smart chips` option
import json
import requests
import urllib.parse
import re

def make_request(email):
    response = requests.post(url=URL, headers=HEADERS, cookies=cookies, data=generate_payload(email=email))

    return response.text

def generate_payload(email):
    quoted_data = urllib.parse.quote(fr'[[["wiDBGd","[[[3,3,\"1\",33]],[null,null,null,\"{email}\"],[1,4,2],[null,\"{email}\"]]",null,"generic"]]]')
    body = f"f.req={quoted_data}&at=AGDSmKtQpLJcPtykN-m9Opky0V-H%3A1709638847739&"

    return body

# 
URL = "https://contacts.google.com/_/SocialPeopleHovercardUi/data/batchexecute?rpcids=wiDBGd&source-path=%2Fwidget%2Fhovercard%2Fv%2F2&hl=en-GB"
COOKIES_FILENAME = "cookies.json"
HEADERS = {
  'authority': 'contacts.google.com',
  'accept': '*/*',
  'accept-language': 'en,en-US;q=0.9',
  'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
  'origin': 'https://contacts.google.com',
  'referer': 'https://contacts.google.com/',
  'sec-ch-ua-mobile': '?0',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'x-same-domain': '1'
}

with open(COOKIES_FILENAME, "r") as cookies_file:
    cookies = json.load(cookies_file)

# ############################################### #
def main(email):
    # email = input("Please enter email to test: ")
    response_data = make_request(email)
    matched_data = re.findall(r"\[.+\]", response_data)

    if matched_data:
        clean_data = matched_data[0]
        parsed_data = json.loads(clean_data)
        email_data = parsed_data[0][2]
        parsed_email_data = json.loads(email_data)

        # if parsed_email_data[1][17]:
        if parsed_email_data[1][1]:
            response = {
                "email": email,
                "name": parsed_email_data[1][0][0],
                "image": parsed_email_data[1][1][0],
                "status": "valid"
            }
        else:
            response = {
                "email": email,
                "status": "not-valid"
            }
    
        return response

