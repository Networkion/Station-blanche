#!/usr/bin/env python3
# coding:utf-8

from pymongo import MongoClient
from dotenv import load_dotenv
import os
import get_hash

class verifyHash(object):

    def query_in_database(self) -> str:
        """
        Query to NoSQL database
        """
        file_hash: str = self.get_hash.FileHash.get_hash()

        mongo_client: str = MongoClient('127.0.0.1', 27027)
        mongo_db: str = mongo_client['whitestation_db']

        collection: str = mongo_db['hash_collection']
        
        result_query: str = collection.find_one({'Query': os.getenv('QUERY')})
        return result_query

    def compare_hash(self, result_query: str, file_hash: str) -> str:
        """
        Compare hash in database
        """

        if not result_query:
            assert ValueError(f"{file_hash} is not found")
        else:
            return "[>] Hash found ! Malware detected."