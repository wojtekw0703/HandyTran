from googletrans import Translator
import win10toast
import time
import pyperclip

toaster = win10toast.ToastNotifier()
sentence = pyperclip.paste()
translator = Translator()

translated_sentence = translator.translate(sentence, src="en", dest="pl")
toaster.show_toast("Tłumacz HandyTran", translated_sentence.text, duration=4)
