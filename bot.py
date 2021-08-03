import os
import requests
import time
tbgs = requests.Session()
url = "https://tbgforums.com/forums/"
cnt = 0
form = {"form_sent": "1"}
form["req_username"] = os.getenv("TBGS_USERNAME")
form["req_password"] = os.getenv("TBGS_PASSWORD")
form["login"] = "Login"
tbgs.post(url+"login.php?action=in", data=form)
form = {"form_sent": "1"}
form["req_message"] = os.getenv("TBGS_MESSAGES")
while True:
    cnt += 1
    res = tbgs.post(url+"post.php?tid=5607", data=form)
    print("Post {} sent.".format(cnt))
