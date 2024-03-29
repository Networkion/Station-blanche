#!/usr/bin/env python3
# coding:utf-8

from colorama import Fore
from pymongo import MongoClient
from .get_hash import FileHash


class VerifyHash(object):
    def __init__(self, path):
        self.file_hash = FileHash().get_hash(path)

    def compare_hash(self, file_hash: str):
        """
        Compare hash in database
        """
        result_query = self.query_in_database(file_hash)
        if not result_query:
            print(Fore.GREEN + f"[+] The hash '{file_hash}' is not found")
        else:
            print(Fore.RED + "[>] Hash found! Malware detected.")

    @staticmethod
    def query_in_database(file_hash: str):
        """
        Query to NoSQL database
        """
        try:
            mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
            db = mongo_client["hashes_database"]
            collection = db["hash_collection"]
            result_query = collection.find_one({"hash": file_hash})

            if result_query:
                return result_query
            else:
                return None
        except Exception as e:
            print(Fore.RED + f"Error querying database: {e}")
            return None
