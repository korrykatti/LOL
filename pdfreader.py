import pyttsx3
# import speech_recognition as sr
from gtts import gTTS
import datetime


from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

#from lol import speak




engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 160)
#print(voices)
engine.setProperty('voice', voices[11].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

from io import StringIO

print("The speaking may take time and that depends on file size and your system specs . For e.g. A pdf of 40 pages took me 25 minutes on a 1 gb pentium")
a = input("Enter pdf file name with extenstion : \n")

output_string = StringIO()
with open(a, 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

speak(output_string.getvalue())