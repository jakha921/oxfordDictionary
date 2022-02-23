import requests
from pprint import pprint


app_id = "598b41f4"
app_key = "74d0cf1dd47096ae58c2d2ba099fbf9f"
language = "en-gb"


def getDefinition(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    results = r.json()
    
    if 'error' in results.keys():
        return False
    

    output = {}
    senses = results['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append("👉" + sense['definitions'][0])
    output['definitions'] = "\n".join(definitions)
    
    if results['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = results['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    
    return output
    
    
if __name__ == '__main__':
    pprint(getDefinition('python'))
    pprint(getDefinition('Jakha'))
    
    
    