#!/usr/bin/env python3
# coding:utf-8

import argparse
import os

from colorama import Fore

# Modules
from modules.scan.get_hash import FileHash
from modules.scan.compare_hash import VerifyHash
from modules.yara.scan_yara import Scanner


def arg_parse():
    """
    Create parser for CLI utilisation
    """
    parser = argparse.ArgumentParser(description="WhiteStation v1.0, script for scan with YARA rules, hashtable, \
                                                 and generate a report PDF")
    parser.add_argument('-f', '--file', help="Provide a single file", type=str)
    parser.add_argument('-d', '--directory', help="Provide a directory")
    parser.add_argument('-y', '--yara', action="store_true", help="Use YARA rules for executable (exe)")
    parser.add_argument('-s', '--scan', action="store_true", help="Scan with Hashtable")
    return parser.parse_args()


def process_input(path, yara, scan):
    """
    Process input
    :param path: Path to the file or dir
    :param yara: Scanning with Yara rules
    :param scan: Scanning with hashTable
    """
    path = os.path.abspath(path)

    if os.path.exists(path):
        if os.path.isfile(path):
            if scan:
                print(Fore.BLUE + "[+] Scanning with Hashtable:", path)
                file_hash = FileHash().get_hash(path)
                VerifyHash(path).compare_hash(file_hash)

            if yara:
                print(Fore.YELLOW + "[+] Yara rules will be used:", path)
                file_hash = FileHash().get_hash(path)
                Scanner().scan_file(path, file_hash)

        elif os.path.isdir(path):
            if scan:
                print(Fore.CYAN + "[+] Scanning files in directory:", path)
                for root, dirs, files in os.walk(path):
                    for file in files:
                        file_path = str(os.path.join(root, file))
                        print(Fore.BLUE + "[+] Scanning with Hashtable:", file_path)
                        file_hash = FileHash().get_hash(file_path)
                        VerifyHash(file_path).compare_hash(file_hash)

            if yara:
                print(Fore.CYAN + "[+] Yara rules will be used for files in directory:", path)
                for root, dirs, files in os.walk(path):
                    for file in files:
                        file_path = str(os.path.join(root, file))
                        print(Fore.YELLOW + "[+] Yara rules will be used for file:", file_path)
                        file_hash = FileHash().get_hash(file_path)
                        Scanner().scan_file(file_path, file_hash)
    else:
        print(Fore.RED + "[-] File or directory not found:", path)


def main(parser):
    """
    Main function
    :param parser: argument parser
    :return:
    """
    if parser.file:
        process_input(parser.file, parser.yara, parser.scan)

    if parser.directory:
        process_input(parser.directory, parser.yara, parser.scan)


if __name__ == "__main__":
    options = arg_parse()
    main(options)
