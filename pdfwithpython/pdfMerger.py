import sys

from PyPDF2 import PdfReader, PdfWriter

file = sys.argv[1:]


def pdf_merger(pdf_list):
    merger = PdfWriter()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('../assets/super.pdf')


# Add water mark to output file
stamp = PdfReader('../assets/wtr.pdf')
template = PdfReader('../assets/super.pdf')
output = PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(stamp.pages[0])
    output.add_page(page)

with open('../assets/out.pdf', 'wb') as file:
    output.write(file)

pdf_merger(file)
