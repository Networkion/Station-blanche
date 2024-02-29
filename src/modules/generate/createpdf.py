#!usr/bin/env python3
# coding:utf-8

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from typing import List


class PdfCreator(object):

    def __init__(self):
        self.doc = None

    @staticmethod
    def create_pdf(file_name: str) -> None:
        doc = SimpleDocTemplate(file_name, pagesize=letter)
        story: List[str] = []

        # Title
        title_style: object = ParagraphStyle(name="TitleStyle", fontSize=30, alignment=1, underline=True,
                                             textColor=colors.black)
        title_text: str = "Whitestation report"
        title_paragraph: object = Paragraph(title_text, title_style)
        story.append(title_paragraph)

        # Create PDF
        doc.build(story)
