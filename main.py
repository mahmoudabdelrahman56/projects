import pyttsx3
import PyPDF2

book = open('the_horse-stealers_and_other_stories._the_tales_of_chekhov_x.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()


for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()