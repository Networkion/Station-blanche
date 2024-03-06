#!/usr/bin/env python3
# coding:utf-8

import argparse
import os

# Modules
from modules.scan.get_hash import FileHash
from modules.scan.compare_hash import VerifyHash
from modules.yara.scan_yara import Scanner
from modules.generate.create_pdf import PdfCreator


def arg_parse():
    parser = argparse.ArgumentParser(description="WhiteStation v1.0, script for scan with YARA rules, hashtable, \
                                                 and generate a report PDF")
    parser.add_argument('-f', '--file', help="Provide a single file", type=str)
    parser.add_argument('-d', '--directory', help="Provide a directory")
    parser.add_argument('-y', '--yara', action="store_true", help="Use YARA rules")
    parser.add_argument('-s', '--scan', action="store_true", help="Scan with Hashtable")
    parser.add_argument('-e', '--export', action="store_true", help="Export the report in PDF")
    return parser.parse_args()


def process_input(path, yara, scan, export):
    if os.path.isfile(path) or os.path.isdir(path):
        if scan:
            print("[+] Scanning with Hashtable.")
            file_hash = FileHash().get_hash(path)
            VerifyHash().compare_hash(file_hash, path)

        if yara:
            print("[+] Yara rules will be used.")
            file_hash = FileHash().get_hash(path)
            Scanner().scan_file(path, file_hash)

        if export:
            print("[+] Exporting the report in PDF.")
            PdfCreator().generate_pdf()
    else:
        print("Invalid file or directory path:", path)


def main(parser):
    if parser.file:
        process_input(parser.file, parser.yara, parser.scan, parser.export)

    if parser.directory:
        process_input(parser.directory, parser.yara, parser.scan, parser.export)


if __name__ == "__main__":
    options = arg_parse()
    main(options)
