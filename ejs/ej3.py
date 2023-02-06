import requests
import json

app_id = "3caeceef"
app_key = "91e70c36e510d79dae57a950122fef58"
source_language = "en-gb"
target_language = 'es-es'
word_id = "dog"
url = "https://od-api.oxforddictionaries.com:443/api/v2/translations/" + source_language + "/" + target_language + "/" + word_id.lower()
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

print(json.dumps(r.json(), indent=2))