import json
import requests
from config import TOKEN
from pprint import pprint
from jsonExtract import jsonExtract


app_id = "598b41f4"
app_key = "74d0cf1dd47096ae58c2d2ba099fbf9f"
language = "en-gb"

# word_id = "python"
# url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + \
#     language + "/" + word_id.lower()

# r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
# print(r.status_code)

# results = r.json()

# pprint(results['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])


# extract from json
# audio_file = (jsonExtract(results, "audioFile"))
# print(audio_file[0])


# HW

# find definition
# while results:
# text = results['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['semanticClasses'][0]['text']
# definition = results['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['shortDefinitions'][0]
# print(text + ":\n" + definition)
# res = results['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
# pprint(len(res))

# print(results['results'][0]['lexicalEntries'][0]['entries'][0])


# print all definitions
while True:
    input_word = input("Enter word: " + '\n')
    word_id = input_word
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    # print(r.status_code)

    results = r.json()
    
    for i in range(len(results['results'][0]['lexicalEntries'][0]['entries'][0]['senses'])):
        text = results['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][i]['semanticClasses'][0]['text']
        definition = results['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][i]['shortDefinitions'][0]
        print(text + ":\n" + definition + "\n")
    
    print('do you wanna try one more time? (y/n)')
    break_loop = input()
    if break_loop == 'n':
        break
