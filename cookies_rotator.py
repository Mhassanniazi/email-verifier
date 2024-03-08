import json
import requests

url = "https://contacts.google.com/_/SocialPeopleHovercardUi/data/batchexecute?rpcids=wiDBGd&source-path=%2Fwidget%2Fhovercard%2Fv%2F2&hl=en-GB"
payload = "f.req=%5B%5B%5B%22wiDBGd%22%2C%22%5B%5B%5B3%2C3%2C%5C%221%5C%22%2C33%5D%5D%2C%5Bnull%2Cnull%2Cnull%2C%5C%22junaidchohan143%40gmail.com%5C%22%5D%2C%5B1%2C4%2C2%5D%2C%5Bnull%2C%5C%22junaidchohan143%40gmail.com%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AGDSmKtQpLJcPtykN-m9Opky0V-H%3A1709638847739&"
headers = {
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

cookies_data_file = open("cookies.json", "r+")
parsed_cookies = json.load(cookies_data_file)
response = requests.post(url=url, headers=headers, data=payload, cookies=parsed_cookies)

latest_cookies = dict(response.cookies)
cookies = parsed_cookies | latest_cookies

if cookies:
    cookies_data_file.seek(0);cookies_data_file.truncate()
    json.dump(cookies, cookies_data_file)
    cookies_data_file.close()

    print("-> Cookies Successfully Refreshed!")


# cookies = "SEARCH_SAMESITE=CgQI9pkB; __Secure-ENID=17.SE=SnLQtVBvTZ4t4OwkyuUMoUF3c0Qp5yPbbAHMQ-upDQb5qSDt_VgKXWATYjkFwTX9snsBwu8MSgd1YCQDv9M3Tx2XZVdHh3An4HatOMz24cbFyRw6zSC86--ceIX4g2R8R5a98YBzN0uWF838fxbPlMIu1yCx0cx3843CGE6TcEptiwmcNx0IFP4k-F_eEaI6kMdc_Fsqg5rbg90yVs5GjJ-KJUK7xXvsYDyDADHSMQ1Cfvv9C-PzqeWrsqU9uPRz_uc07X7K3Km-Ff8p3pTSs9wtvsbnMuo60MdFU9zG; SID=g.a000gghwGpNeDbLct6tW-6mcAqBwZN7jXk4txPcpd74ecspDRMkwfRA-28gIB3sH1OEOIz71GgACgYKAcASAQASFQHGX2MibZ2X24rSBZ9z6s7PkBafNBoVAUF8yKoiifG4NPTXQTdfZksL2VwM0076; __Secure-1PSID=g.a000gghwGpNeDbLct6tW-6mcAqBwZN7jXk4txPcpd74ecspDRMkwXUmXuushleGxOOgzyyvTeAACgYKATQSAQASFQHGX2MiOuJqzL3ZhUr9_RaXwlWyTBoVAUF8yKrJoNTjPcUZ_CyO-cQtgJGN0076; __Secure-3PSID=g.a000gghwGpNeDbLct6tW-6mcAqBwZN7jXk4txPcpd74ecspDRMkwqVRfHyrVdCyc6jMLRXORgwACgYKAcMSAQASFQHGX2Mijss0zpfqVkvrmho0NKGjEBoVAUF8yKrwSaKUT-maRzXsbtnIStLU0076; HSID=Ae7HXLxKWMHeISdru; SSID=AnY2MpD-uCe7qbN0u; APISID=XVTZz5aN7JcCd0bC/AcbLTNekw1z10ctof; SAPISID=AAHK0XlikN0GRt9N/Am1_X92q7VWOHiXDY; __Secure-1PAPISID=AAHK0XlikN0GRt9N/Am1_X92q7VWOHiXDY; __Secure-3PAPISID=AAHK0XlikN0GRt9N/Am1_X92q7VWOHiXDY; OTZ=7448708_36_36__36_; 1P_JAR=2024-03-08-05; AEC=Ae3NU9MAyyp0cI1Enwy66yLLJYpYbcQgAp0SpB5_0pHwsw2u4uwqAIje-8A; NID=512=nBcQILogyLTsPU1MheEtRO_CXegLXcO6pakmZwdOpI3no82kY-hUudo5kPaoMS1k3Z-wnE5cMUKb20T7xb7Erx8RVfMMG1VI33Ou5FITkcYW9IxdUO1E8vRGxGnbPzDwtlzcOozrdxz99JhsK0IacDy82LH58n_UmgFblwQsc4obzE0tbPiGV0SCE4pygR6a2zi6vdTIO-bi585tTXYWYkDhdb8zEuYde0wbuII8_vznS5ifPUAntouc4-IUj3I1x5GC8CwXk4Ih7Edx5jTUHlUliSA2drt9dustdT05uRJF3ACWc33v6TmT14rjmYvqnNfRogv44ObZWSFjbA0gWOF8sZsB8uM2GzXhVkkN8cTmcEWIZDgUXDM_d-_BuL5yIMvDuRjgbUR_OQH8Uxo4K6W6rPPSrZNabcSzlcibMAjD08cSzfDWMV4udv2FhGkaKhdD_8PmAHgkjNv_FG8JujoNS4QdKu2vpNCJKuwRh_eMcAsmitzh4jtuXUUdRxbByqade3KyOFt-gQonMVcQN1YIHe2NrSnSkOWXC3jQEFPD8arIb_UySTtefxt0itteBJZoJZmeUisRgsL0kL-eXPL4QA; __Secure-1PSIDTS=sidts-CjIBYfD7Z8xaVttxEdOTF_YRf420BhFTlBph20p4oxKZ3xqShbaM3JriqrH55qTUhk_VnBAA; __Secure-3PSIDTS=sidts-CjIBYfD7Z8xaVttxEdOTF_YRf420BhFTlBph20p4oxKZ3xqShbaM3JriqrH55qTUhk_VnBAA; SIDCC=AKEyXzXlWcmLbmpbJRRu6IuZ7L3IGxuhVhj3dug71DIZURZU5k4Xng5x2uxqIKpUZqPhxlQ1AU00; __Secure-1PSIDCC=AKEyXzUsSbePpHBOOkIn6rk0fP2_ILDAMtHhl5n6Z6AQIVbUDehwpCuStjEXUl9kChY2zmSgiGy0; __Secure-3PSIDCC=AKEyXzWODnd8mlcPjgtmKIQcvzReB2rIw4JeHCnlXezP0MPW-JnTRWzPMkn_6IarRy_5pvzi3cbH"
# data_dict = {}
# for item in cookies.split(";"):
#     split_data = item.split("=")
#     key, value = split_data[0], "=".join(split_data[1:])    
#     data_dict[key.strip()] = value

# with open("cookies.json", "w") as file:
#     json.dump(data_dict, file)