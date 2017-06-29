from urllib2 import *
import urllib
import json
import sys

API_KEY="AIzaSyBOTaWUvzwtWHfEpZ8zH8d-31aKZn6k4Po"

messageTitle = sys.argv[1]
messageBody = sys.argv[2]

data={
    "to" : "/topics/my_little_topic",
    "notification" : {
        "body" : messageBody,
        "title" : messageTitle,
        "icon" : "ic_cloud_white_48dp"
    }
}

dataAsJSON = json.dumps(data)

request = Request(
    "https://gcm-http.googleapis.com/gcm/send",
    dataAsJSON,
    { "Authorization" : "key="+API_KEY,
      "Content-type" : "application/json"
    }
)

print urlopen(request).read()
