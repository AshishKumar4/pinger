#!/usr/bin/python3

import requests
import time

def Logic():
    try:
        while True:
            try:
                requests.get("http://13.232.194.111:80/verify/d3261fa60c79562a4b717f3bd3420ccc")
                time.sleep(1*60)
            except Exception as e:
                print("Error inside loop!", e)
    except Exception as e:
        print("Error in logic ! ", e)
        Logic()


Logic()