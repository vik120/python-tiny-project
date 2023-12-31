from PyPDF2 import PdfReader
# reader = PdfReader('../assets/100KB.pdf')
# print(len(reader.pages))

with open('../assets/350KB.pdf', 'rb') as file:
    readFile = PdfReader(file)
    print(len(readFile.pages))

