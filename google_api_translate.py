import yaml
import six
import time
from google.cloud import translate_v2 as translate
# from google.cloud import translate

def read_file(src_file):    
    with open(src_file) as file:        
       return yaml.load(file, Loader=yaml.FullLoader)        

def write_file(dst_file, data):
    with open(dst_file, 'w', encoding="utf-8") as file:
        yaml.dump(data, file, allow_unicode=True)

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """


    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)
    print(result)

    return result["translatedText"]
    

if __name__ == "__main__":
    r_file = "~/src_language_emojis_OpenShot-Emojis-be.po"
    w_file = '~/google_translated.yaml'
   
    final = []
    res = ""
    data = read_file(r_file)

    for item in data:
        # print("translating:", item['msgid'])
        if  item['msgstr'] == "":
            res = translate_text('be', item['msgid'])            
        # print("got results: ", res)

        item['msgstr'] = res.capitalize()
        final.append(item)
        
        write_file(w_file, final)
        
        time.sleep(0.8)
  
    write_file(w_file, final)    


# final genaration .to files
if __name__ == "__main__":
    res = []
    
    r_file = '~/results.yaml'
    data = read_file(r_file)
    for item in data:
        print('#: Emoji Metadata (Displayed Name)')
        print('msgid "{}"'.format(item['msgid']))
        print('msgstr "{}"'.format(item['msgstr']))
        print()
