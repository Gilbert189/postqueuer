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
tbgs.post(url + "login.php?action=in", data=form)
form = {"delete": "Delete"}
for i in range(568733, 569356):
    cnt += 1
    tbgs.post(url + "delete.php?id=" + str(i), data=form)
    print("Post {} deleted.".format(i))
