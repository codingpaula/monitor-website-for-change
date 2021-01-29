import os
import requests    # to download page
from bs4 import BeautifulSoup    # to parse what we download
import time    # to add delay between runs
import smtplib    # to allow us to email


url = "https://www.carved.com/collections/custom-block-live-edges-all"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,  "lxml")
    
if str(soup).find("card-product") > -1:
    if os.environ['ALREADYSENT'] is '0':
        msg = 'Subject: script found new live edge case!!'
        fromaddr = 'codingpaula@gmail.com'
        toaddrs = ['paula.ritter@protonmail.com']

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, os.environ['MAILTOKEN'])
    
        print(time.localtime())
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)
    
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
            
        os.environ['ALREADYSENT'] = '1'
else:
    os.environ['ALREADYSENT'] = '0'
    print('no live edge case was found')
    
time.sleep(300)
