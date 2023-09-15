#!usr/bin/env python3.11
#coding:utf-8

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class createPDF:
    def create_pdf(file_name):
        c = canvas.Canvas(file_name, pagesize=letter)
        width, height = letter

        c.drawString(100, height - 100, "Génération de PDF par python set-up !")
        c.save()