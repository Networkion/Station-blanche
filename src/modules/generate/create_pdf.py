#!usr/bin/env python3
# coding:utf-8

import pdfkit


class PdfCreator(object):

    @staticmethod
    def generate_pdf(input_file, output_file):
        options = {
            'header-html': 'header.html',
            'footerhtml': 'footer.html'
        }
        pdfkit.from_file(input_file, output_file, options=options)


if __name__ == "__main__":
    creator = PdfCreator()
    input_html = './template/template.html'
    output_pdf = 'output.pdf'
    creator.generate_pdf(input_html, output_pdf)
