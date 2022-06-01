"""A simple post queuer for the TBGs."""


import os
import requests
import time
from celery import Celery
from bs4 import BeautifulSoup as bs 


if sys.argv[0].endswith("celery"): # ensures this code is run only when using celery
    # Not sure why Tony doesn't store these on variables.
    # Is this a security thing or is it just Tony being lazy?
    USERNAME = os.getenv("TBGS_USERNAME")
    PASSWORD = os.getenv("TBGS_PASSWORD")

    tbgs = requests.Session()
    url = "https://tbgforums.com/forums/"

    # Login to the TBGs
    form = {"form_sent": "1"}
    form["req_username"] = USERNAME
    form["req_password"] = PASSWORD

    form["login"] = "Login"
    tbgs.post(f"{url}login.php?action=in", data=form)


# Buy some celery
BROKER = os.getenv("QUEUER_BROKER")
BACKEND = os.getenv("QUEUER_BACKEND")
queuer = Celery("postqueuer", backend=BACKEND, broker=BROKER)


@queuer.task
def post(msg: str, topic_id: int) -> tuple:
    global tbgs
    
    # Make sure the tbgs variable exists
    if "tbgs" not in globals():
        raise RuntimeError("Can't run this function locally")
    
    form = {"form_sent": "1"}
    form["req_message"] = msg
    res = tbgs.post(f"{url}post.php?tid={topic_id}", data=form)
    
    # Check for errors
    tree = bs(res.text)
    error = tree.find(id="posterror")
    if error:
        error = error.findall("strong")
        error = [x.text for x in error]
        raise RuntimeError(error)
    return {"status": res.status_code, "content": res.content}
