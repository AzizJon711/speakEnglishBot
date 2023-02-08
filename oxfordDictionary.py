import  requests
import json

app_id = '4c483136'
app_key = '40d3c2aff35d1199dd8011000d5643f5'
language = 'en-gb'

def getDefinitions(word_id):
    try:
        url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/' + word_id.lower()
        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        r = r.json()
        definitions = []
        for definition in r["results"]:
            for i in definition["lexicalEntries"]:
                for j in i["entries"]:
                    for k in j["senses"]:
                        definitions.append(k["definitions"][0])
        return definitions
    except:
        return ["No such word exists!"]
def getAudiofile(word_id):
    try:
        url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/' + word_id.lower()
        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        r = r.json()
        audio = r["results"][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["audioFile"]
        return audio
    except:
        return "Bunday so'z mavjud emas!"
