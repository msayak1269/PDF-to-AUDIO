import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()

pdf_reader = PyPDF2.PdfFileReader(book)

num_pages = pdf_reader.numPages

play_book = pyttsx3.init()

print("Playing Audio......")

for num in range(0,num_pages):

	page = pdf_reader.getPage(num)

	text = page.extractText()

	play_book.say(text)

	play_book.runAndWait()

