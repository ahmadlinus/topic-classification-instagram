# topic-classification-instagram
A small project for topic classification of instagram posts. Given a piece of text, it will give back a probability distribution over different topics. 

The app has been deployed to [this address](https://topic-classifier.azurewebsites.net/) on Azure App service. To use the endpoint, you can use curl to invoke the REST endpoint. 


```
curl \
-d '{"text": "The socio-political stability of the region seems to be endangered by deeply grounded hostility from all sides."}' \
-H "Content-Type: application/json" \
-X POST https://topic-classifier.azurewebsites.net/topics
```

You should receive a response like this:

```
{
'Sport': 0.7340793790951522,
'Art': 0.024463561800317182,
'Politics': 0.13717563647532585,
'Food': 0.10428142262920488
}
```

Alternatively, you can use the endpoint with an HTTP client (like requests on Python), you will see an example below:


```
import requests

headers = {"Content-Type": "application/json"}
data = {"text": "The socio-political stability of the region seems to be endangered by deeply grounded hostility from all sides."}
url = "https://topic-classifier.azurewebsites.net/topics"

try:
  r = requests.post(url, json=data, headers=headers)
  r.raise_for_status()
  print(r.json())

except:
  pass
```

