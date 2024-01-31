#!usr/bin/env python3.11
#coding:utf-8

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

class createPDF:
    def create_pdf(file_name):
        doc = SimpleDocTemplate(file_name, pagesize=letter)
        story = []

        # Style pour le titre
        title_style = ParagraphStyle(name="TitleStyle", fontSize=30, alignment=1, underline=True, textColor=colors.black)

        # Ajouter le titre centré
        title_text = "Networkion - Whitestation report"
        title_paragraph = Paragraph(title_text, title_style)
        story.append(title_paragraph)
        
        # Créer le PDF
        doc.build(story)