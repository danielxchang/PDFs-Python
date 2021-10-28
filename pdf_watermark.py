import PyPDF2

def watermark_pages(template, watermark, writer):
     for page_num in range(template.getNumPages()):
          page = template.getPage(page_num)
          page.mergePage(watermark.getPage(0))
          writer.addPage(page)

def main():
     template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
     watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
     writer = PyPDF2.PdfFileWriter()

     watermark_pages(template, watermark, writer)
     writer.write(open('watermarked_file.pdf', 'wb'))

if __name__ == "__main__":
     main()