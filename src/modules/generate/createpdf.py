#!usr/bin/env python3.11
# coding:utf-8

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph


class PDFCreated(object):

    def __init__(self):
        self.doc = None

    @staticmethod
    def create_pdf(file_name: str) -> None:
        doc = SimpleDocTemplate(file_name, pagesize=letter)
        story = []

        # Title
        title_style = ParagraphStyle(name="TitleStyle", fontSize=30, alignment=1, underline=True,
                                     textColor=colors.black)
        title_text = "Whitestation report"
        title_paragraph = Paragraph(title_text, title_style)
        story.append(title_paragraph)

        # Create PDF
        doc.build(story)
