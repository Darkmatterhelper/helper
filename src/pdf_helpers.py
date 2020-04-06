"""
QUIZ REPORTS: pdf_helpers

authors:
@markoprodanovic

last edit:
Monday, April 06, 2020
"""

from reportlab.pdfgen import canvas as pdfcanvas
import settings


def generate_pdf(row, cols, title, pdf_dir_path, anonymous_id):
    pdf = pdfcanvas.Canvas(pdf_dir_path + '/' + f'{title}.pdf')
    # draw_my_ruler(pdf)

    # set title for pdf
    pdf.setTitle(title)

    for c in cols:

        # print anonymous id above each question
        pdf.setFont('Courier-Bold', 14)
        pdf.drawString(50, 760, anonymous_id)
        pdf.setFont('Courier', 14)
        pdf.drawString(50, 740, settings.course.name)

        lines = 0
        text = pdf.beginText(50, 700)
        text.setFont('Courier', 12)

        # add question text
        text, lines, pdf = wrap_text_line(text, c, lines, pdf)

        # add space
        text.textLine(' ')
        lines += 1

        # add student response
        text, lines, pdf = wrap_text_line(text, str(row[c]), lines, pdf)
        pdf.drawText(text)

        # add page break for next question/response
        pdf.showPage()
        lines = 0

    # save pdf
    pdf.save()


def wrap_text_line(pdf_txt, raw_txt, lines, pdf):
    while len(raw_txt) > 0:

        if (lines >= 45):
            pdf.drawText(pdf_txt)
            pdf.showPage()
            pdf_txt = pdf.beginText(50, 750)
            pdf_txt.setFont('Courier', 12)
            lines = 0

        # take off the first 70 characters from str
        if len(raw_txt) <= 60:
            pdf_txt.textLine(raw_txt)
            lines += 1
            return pdf_txt, lines, pdf
        else:
            line = raw_txt[0:60]
            raw_txt = raw_txt[60:]

            if ' ' in raw_txt:
                split = raw_txt.split(' ', 1)
                line = line + split[0]
                raw_txt = split[1]
            else:
                line = line + raw_txt
                raw_txt = ''

            pdf_txt.textLine(line)
            lines += 1

    return pdf_txt, lines, pdf


def draw_my_ruler(pdf):
    pdf.drawString(100, 810, 'x100')
    pdf.drawString(200, 810, 'x200')
    pdf.drawString(300, 810, 'x300')
    pdf.drawString(400, 810, 'x400')
    pdf.drawString(500, 810, 'x500')

    pdf.drawString(10, 100, 'y100')
    pdf.drawString(10, 200, 'y200')
    pdf.drawString(10, 300, 'y300')
    pdf.drawString(10, 400, 'y400')
    pdf.drawString(10, 500, 'y500')
    pdf.drawString(10, 600, 'y600')
    pdf.drawString(10, 700, 'y700')
    pdf.drawString(10, 800, 'y800')
