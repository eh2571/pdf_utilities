from PyPDF2 import PdfFileReader, PdfFileWriter

file_input = input("Enter file name: ")
file_output = input("Enter file output: ")

# for page in range(1,10):
#     file_input = f"lecture{page}.pdf"
#     file_output = f"lec{page}.pdf"

with open(file_input, 'rb') as infile:
    pdf = PdfFileReader(infile)
    pgnums = pdf.trailer["/Root"]["/PageLabels"]["/Nums"]
    pgs = pgnums[slice(0, len(pgnums), 2)]
    pgs = [0] + [x-1 for x in pgs[2:len(pgs)]] + [pdf.getNumPages()-1]

    writer = PdfFileWriter()
    for pg in pgs:
        writer.addPage(pdf.getPage(pg))

        with open(file_output, 'wb') as outfile:
            writer.write(outfile)

print(f"Finished saving logical pages from {file_input} to {file_output}")