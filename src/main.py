#!/usr/bin/env python3
# coding:utf-8

import argparse

# Modules
from modules.scan.get_hash import FileHash
from modules.scan.compare_hash import VerifyHash
from modules.yara.scan_yara import Scanner
from modules.generate.create_pdf import PdfCreator


def arg_parse():
    parser = argparse.ArgumentParser(description="WhiteStation v1.0, script for scan with YARA rules, hashtable, \
                                                 and generate a report PDF")
    parser.add_argument('-f', '--file', help="Provide a single file")
    parser.add_argument('-d', '--directory', help="Provide a directory")
    parser.add_argument('-y', '--yara', action="store_true", help="Use YARA rules")
    parser.add_argument('-s', '--scan', action="store_true", help="Scan with Hashtable")
    parser.add_argument('-e', '--export', action="store_true", help="Export the report in PDF")
    return parser.parse_args()


def main(parser):
    if parser.scan:
        print("[+] Scanning with Hashtable.")
        file_hash = FileHash.get_hash(parser.directory)
        VerifyHash.compare_hash(file_hash)

    if parser.yara:
        print("[+] Yara rules will be used.")
        Scanner.scan_file(parser.file)

    if parser.export:
        print("[+] Exporting the report in PDF.")
        PdfCreator.generate_pdf()


if __name__ == "__main__":
    options = arg_parse()
    main(options)
