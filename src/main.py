#!/usr/bin/env python3
import argparse

modules_path = [
    "./src/modules/generate",
    "./src/modules/yara",
]


def arg_parse():
    parser = argparse.ArgumentParser(description="A script for performing certain actions.")
    parser.add_argument('-y', '--yara', action="store_true", help="Use yara rules")
    parser.add_argument('-s', '--scan', action="store_true", help="Scan with Hashtable")
    parser.add_argument('-e', '--export', action="store_true", help="Export the report in PDF")
    return parser.parse_args()


def main(parser):
    if parser.yara:
        print("[+] Yara rules will be used.")

    if parser.scan:
        print("[+] Scanning with Hashtable.")

    if parser.export:
        print("[+] Exporting the report in PDF.")


if __name__ == "__main__":
    options = arg_parse()
    main(options)
