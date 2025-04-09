from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from translate import Translator

# Mapping language names to ISO 639-1 codes
LANGUAGE_CODES = {
    "Hindi": "hi",
    "Marathi": "mr",
    "German": "de",
    "Urdu": "ur",  # ✅ Correct language code for Urdu
}

def home(request): 
    if request.method == "POST": 
        text = request.POST["translate"] 
        language = request.POST["language"]

        # Get correct ISO code, default to English ("en") if not found
        lang_code = LANGUAGE_CODES.get(language, "en")  

        translator = Translator(to_lang=lang_code) 
        translation = translator.translate(text) 

        return HttpResponse(translation)  

    return render(request, "main/index.html")

