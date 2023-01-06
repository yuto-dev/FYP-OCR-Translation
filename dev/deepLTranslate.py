import deepl
from authKey import auth_key

 # Replace with your key
translator = deepl.Translator(auth_key)

result = translator.translate_text("Halo, Dunia!", target_lang="EN-US")
print(result.text)