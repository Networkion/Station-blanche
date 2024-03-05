#!usr/bin/env python3
# coding:utf-8

import os
from pymongo import MongoClient
from yara_scanner import YaraScanner


class Scanner(object):

    def __init__(self):
        self.scanner = YaraScanner()
        self.scanner.track_yara_dir('modules/yara/rules')
        self.client, self.db, self.collection = self.database_info()

    @staticmethod
    def database_info():
        client = MongoClient("mongodb://127.0.0.1:27017/")
        db = client["hashes_database"]
        collection = db["hash_collection"]
        return client, db, collection

    def load_rules(self):
        self.scanner.load_rules()
        return "Rules loaded"

    def scan_file(self, directory: str, file_hash: str) -> str:
        directory = os.path.abspath(directory)

        if self.scanner.scan(directory):
            if self.scanner.scan_results:
                self.collection.insert_one({"hash": file_hash})
                return "[>] Malware detected by YARA rules!"
            else:
                return "[!] No malware detected."
        else:
            raise Exception("[-] Error occurred during scanning.")
