# importing the modules
import PyPDF2
import pyttsx3
  
# path of the PDF file

a = input("Enter PDF FILE NAME : ")
path = open(a, 'rb')

i = 0
  
# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)
  
# the page with which you want to start
def read():
    from_page = pdfReader.getPage(0-i)
  
# extracting the text from the PDF
text = from_page.extractText()

print(text) 
# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()

re


voices = speak.getProperty('voices')

speak.setProperty('rate', 120)
#print(voices)
speak.setProperty('voice', voices[56].id)