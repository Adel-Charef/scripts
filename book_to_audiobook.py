import PyPDF2
import pyttsx3

poem_book = open("poem.pdf", "rb")


def readOutLoud(book):

    pdf_reader = PyPDF2.PdfFileReader(book)
    num_pages = pdf_reader.numPages

    play = pyttsx3.init()
    print("Playing Audiobook...")

    for num in range(0, num_pages):
        page = pdf_reader.getPage(num)
        data = page.extractText()
        play.setProperty("rate", 130)
        play.say(data)
        play.runAndWait()

    print("Done Reading....")

readOutLoud(poem_book)
