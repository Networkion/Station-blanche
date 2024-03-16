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
    """
    Create parser for CLI utilisation
    """
    parser = argparse.ArgumentParser(description="WhiteStation v1.0, script for scan with YARA rules, hashtable, \
                                                 and generate a report PDF")
    parser.add_argument('-f', '--file', help="Provide a single file", type=str)
    parser.add_argument('-d', '--directory', help="Provide a directory")
    parser.add_argument('-y', '--yara', action="store_true", help="Use YARA rules")
    parser.add_argument('-s', '--scan', action="store_true", help="Scan with Hashtable")
    parser.add_argument('-e', '--export', action="store_true", help="Export the report in PDF")
    return parser.parse_args()


def process_input(path, yara, scan, export):
    """
    Process input
    :param path: Path to the file or dir
    :param yara: Scanning with Yara rules
    :param scan: Scanning with hashTable
    :param export: Export in PDF the result
    """
    if os.path.isfile(path):
        if scan:
            print("[+] Scanning with Hashtable.")
            file_hash = FileHash().get_hash(path)
            return VerifyHash(path).compare_hash(file_hash)

        if yara:
            print("[+] Yara rules will be used.")
            file_hash = FileHash().get_hash(path)
            return Scanner().scan_file(path, file_hash)

        if export:
            print("[+] Exporting the report in PDF.")
            PdfCreator().generate_pdf()

    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = str(os.path.join(root, file))
                if scan:
                    print("[+] Scanning with Hashtable:", file_path)
                    file_hash = FileHash().get_hash(file_path)
                    VerifyHash(file_path).compare_hash(file_hash)

                if yara:
                    print("[+] Yara rules will be used:", file_path)
                    file_hash = FileHash().get_hash(file_path)
                    Scanner().scan_file(file_path, file_hash)

                if export:
                    print("[+] Exporting the report in PDF for:", file_path)
                    PdfCreator().generate_pdf()


def main(parser):
    """
    Main function
    :param parser: argument parser
    :return:
    """
    if parser.file:
        process_input(parser.file, parser.yara, parser.scan, parser.export)

    if parser.directory:
        process_input(parser.directory, parser.yara, parser.scan, parser.export)


if __name__ == "__main__":
    options = arg_parse()
    main(options)
