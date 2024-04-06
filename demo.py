
from pdfTable import PdfTable
from data import data, data2, data3, data4

pdf = PdfTable()
pdf.add_page()
pdf.createTable(data)
pdf.multi_cell(w=5,h=15, text="")
pdf.createTable(data2)
pdf.multi_cell(w=5,h=15, text="")
pdf.createTable(data3)
pdf.multi_cell(w=5,h=15, text="")
pdf.createTable(data4)
pdf.output('./reports/table.pdf')
