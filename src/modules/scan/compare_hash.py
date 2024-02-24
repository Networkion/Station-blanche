#!/usr/bin/env python3
# coding:utf-8

from pymongo import MongoClient
import os


class VerifyHash(object):
    @staticmethod
    def compare_hash(result_query: str, file_hash: str) -> str:
        """
        Compare hash in database
        """

        if not result_query:
            assert ValueError(f"{file_hash} is not found")
        else:
            return "[>] Hash found ! Malware detected."

    def __init__(self):
        self.get_hash = None

    def query_in_database(self) -> str:
        """
        Query to NoSQL database
        """
        self.get_hash.FileHash.get_hash()

        mongo_client = MongoClient('127.0.0.1', 27027)
        mongo_db = mongo_client['whitestation_db']

        collection = mongo_db['hash_collection']

        result_query: str = collection.find_one({'Query': os.getenv('QUERY (???)')})
        return result_query
