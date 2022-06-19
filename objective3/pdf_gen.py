# def pdf_gen():
import csv
from fpdf import FPDF
# from sum import *

with open('questions_generated.csv', newline='') as f:
    reader = csv.reader(f)

    pdf = FPDF()
    pdf.add_page()
    page_width = pdf.w - 2 * pdf.l_margin

    pdf.set_font('Times', 'B', 18.0)
    pdf.cell(page_width, 0.0, 'PESITM, Department of CSE ', align='C')

    pdf.ln(10)

    pdf.set_font('Courier', '', 12)

    col_width = page_width/ 4

    pdf.ln(3)

    th = pdf.font_size

    for row in reader:
        # print(row)
        pdf.cell(col_width, th, str(row[0]), border=1)
        pdf.cell(col_width, th, row[1], border=1)
        pdf.cell(col_width, th, row[2], border=1)
        pdf.cell(col_width, th, row[3], border=1)
        pdf.cell(col_width, th, row[4], border=1)
        pdf.ln(th)

    pdf.ln(10)

    pdf.set_font('Times', '', 10.0)

    pdf.cell(page_width, 0.0, '- Thank you -', align='C')

    pdf.output('question_generated.pdf', 'F')
