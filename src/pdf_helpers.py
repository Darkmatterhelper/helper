"""
QUIZ REPORTS: pdf_helpers

authors:
@markoprodanovic

last edit:
Monday, May 04, 2020
"""

from reportlab.pdfgen import canvas as pdfcanvas
import settings


def generate_pdf(row, cols, title, pdf_dir_path, anonymous_id):
    filename = f"{title}.pdf"
    target = pdf_dir_path / filename
    pdf = pdfcanvas.Canvas(str(target))
    # draw_my_ruler(pdf)

    # set title for pdf
    pdf.setTitle(title)

    for c in cols:

        # print anonymous id above each question
        pdf.setFont("Courier-Bold", 14)
        pdf.drawString(50, 760, anonymous_id)
        pdf.setFont("Courier", 14)
        pdf.drawString(50, 740, settings.course.name)

        lines = 0
        text = pdf.beginText(50, 700)
        text.setFont("Courier", 12)

        # add question text
        if settings.include_questions:
            text, lines, pdf = wrap_text_line(text, c, lines, pdf)

        # add space
        text.textLine(" ")
        lines += 1

        # add student response if one is there, otherwise print a blank below the question
        if str(row[c]) != "nan":
            text, lines, pdf = wrap_text_line(text, str(row[c]), lines, pdf)

        pdf.drawText(text)

        # add page break for next question/response
        pdf.showPage()
        lines = 0

    # save pdf
    pdf.save()


def wrap_text_line(pdf_txt, raw_txt, lines, pdf):
    while len(raw_txt) > 0:

        if lines >= 45:
            pdf.drawText(pdf_txt)
            pdf.showPage()
            pdf_txt = pdf.beginText(50, 750)
            pdf_txt.setFont("Courier", 12)
            lines = 0

        # take off the first 60 characters from str
        if len(raw_txt) <= 60:
            pdf_txt, lines = __draw_text(pdf_txt, raw_txt, lines)
            return pdf_txt, lines, pdf
        else:
            line = raw_txt[0:60]
            raw_txt = raw_txt[60:]

            if " " in raw_txt:
                split = raw_txt.split(" ", 1)
                line = line + split[0]
                raw_txt = split[1]
            else:
                line = line + raw_txt
                raw_txt = ""

            pdf_txt, lines = __draw_text(pdf_txt, line, lines)

    return pdf_txt, lines, pdf


def __draw_text(pdf_txt, raw_txt, lines):
    """
    Handles the display of paragraphs in the PDF
    """
    paragraphs = raw_txt.split("\n")

    for p in paragraphs:
        if p == "\n":
            pdf_txt.textLine(" ")
            lines += 1
            continue

        pdf_txt.textLine(p)
        lines += 1

    return pdf_txt, lines


def draw_my_ruler(pdf):
    pdf.drawString(100, 810, "x100")
    pdf.drawString(200, 810, "x200")
    pdf.drawString(300, 810, "x300")
    pdf.drawString(400, 810, "x400")
    pdf.drawString(500, 810, "x500")

    pdf.drawString(10, 100, "y100")
    pdf.drawString(10, 200, "y200")
    pdf.drawString(10, 300, "y300")
    pdf.drawString(10, 400, "y400")
    pdf.drawString(10, 500, "y500")
    pdf.drawString(10, 600, "y600")
    pdf.drawString(10, 700, "y700")
    pdf.drawString(10, 800, "y800")
