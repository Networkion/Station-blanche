#!/usr/bin/env python3
# coding:utf-8

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
            raise ValueError(f"{file_hash} is not found")
        else:
            print("[>] Hash found ! Malware detected.")

    @staticmethod
    def query_in_database(file_hash: str) -> str:
        """
        Query to NoSQL database
        """
        mongo_client = MongoClient('mongodb', 27027)
        mongo_db = mongo_client['whitestation_db']

        collection = mongo_db['hash_collection']

        result_query = collection.find_one({"hash": file_hash})
        return result_query
