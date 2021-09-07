# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:10:38 2021

@author: prince
"""

#Demonstrating date time manipulation using datetime
#python has datetime to work with dates and times.
import datetime

datetime_obj = datetime.datetime.now()
print(datetime_obj)

date_object = datetime.date.today()
print(date_object)

print(dir(datetime))

#Writing a multi-threaded countdown timer program
import threading
import time

def hello():
    print("hello, Timer")

if __name__ == '__main__':
    t = threading.Timer(3.0, hello)
    t.start()
    
#Demonstrating API calls through request modules
# When you want to interact with data via a REST API, this is called a request. 
#A request is made up of the following components: endpoint, data , headers, method
pip install requests
import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response)
response.json()

#