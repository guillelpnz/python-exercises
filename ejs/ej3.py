import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

source_language = "en-gb"
target_language = 'es-es'

# Function that tries to access the received dictionary in two different ways
# It's necessary because translations and examples are not accurate / don't exist with only one way 
def try_dictionary_access(dictionary, subsenses, tries=3):
    i = 0
    translation_msg = ""
    
    examples = []
    while i < tries:
        try:
            if subsenses:
                translation = dictionary['results'][i]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['translations'][0]['text']
                examples = dictionary['results'][i]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['examples']
            else:
                translation = dictionary['results'][i]['lexicalEntries'][0]['entries'][0]['senses'][0]['translations'][0]['text']
                examples = dictionary['results'][i]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples']
            translation_msg = f"La palabra inglesa '{dictionary['id']}' se puede traducir como '{translation}'"
            break
        except (KeyError, IndexError):
            i += 1
            continue

    return translation_msg, examples

# Build the final string
def get_full_msg(translation_msg, examples):
    final_msg = f"{translation_msg}\n"
    if examples:
        final_msg += "Algunas oraciones con esta palabra: \n"
    for i, example in enumerate(examples):
        final_msg += f"{chr(97+i)}. {example['text']}\n"

    return final_msg

# Function that calls the api. Returns translations and examples
def try_endpoint(url, app_id, app_key, word_id):
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    if r.status_code == 200:
        res_json = r.json()

        # Try accessing ['senses'] -> Better translations if they exist
        translation_msg_and_examples = try_dictionary_access(res_json, False)
        
        if translation_msg_and_examples[0]:
            return translation_msg_and_examples
        else:
            # Try accessing ['subsenses'] -> Alternative if ['senses'] does not exist in dictionary
            translation_msg_and_examples = try_dictionary_access(res_json, True)
            if translation_msg_and_examples[0]:
                return translation_msg_and_examples

        return "Acceso incorrecto al diccionario. Podría haber sido modificado", []
    else:
        return f"Palabra: {word_id} no encontrada en el diccionario", []

if __name__ == '__main__':
    # List of words to test against the function
    word_id_list = ["flower", "sdtytytyfgfgh", "dog"]

    for word_id in word_id_list:
        if not word_id or not isinstance(word_id, str):
            continue

        url = "https://od-api.oxforddictionaries.com:443/api/v2/translations/" + source_language + "/" + target_language + "/" + word_id.lower()
        translation_msg_and_examples = try_endpoint(url, APP_ID, APP_KEY, word_id)
        print(get_full_msg(translation_msg_and_examples[0], translation_msg_and_examples[1]))
