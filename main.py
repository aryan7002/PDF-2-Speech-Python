import pyttsx3 #pip install pyttsx3
import PyPDF2  #pip install pypdf2
book =open('sample.pdf','rb') #change name of pdf
pdfReader = PyPDF2.PdfFileReader(book)
pages= pdfReader.numPages
print(pages)
speak=pyttsx3.init()
for num in range(1,pages):
    page =pdfReader.getPage(1)
    text =page.extractText()
    speak.say(text)
    speak.runAndWait()
