#!/usr/bin/env python3
# coding:utf-8

import hashlib
import os
from typing import List

class getFileHash:

    # Constants
    BUF_SIZE: int = 4096

    @staticmethod

    # Get SHA-256 hash of a file
    def get_hash_file(file_path: str) -> str:
        hash_value = hashlib.sha256()
        with open(file_path, "rb") as file:
            for byte_block in iter(lambda: file.read(getFileHash.BUF_SIZE), b""):
                hash_value.update(byte_block)
        return hash_value.hexdigest()


    # Get SHA-256 hashes of files in a directory
    def get_file_from_directory(directory_path: str) -> List[str]:
        hashes: List[str] = []
        if os.path.isdir(directory_path):
            # Iterate over files in the directory
            for file_name in os.listdir(directory_path):
                file_path = os.path.join(directory_path, file_name)
                # Check if the path is a file
                if os.path.isfile(file_path):
                    # Calculate hash for each file
                    sha256_hash = getFileHash.get_hash(file_path)
                    print(f"[+] SHA256 hash of {file_name}: {sha256_hash}")
                    hashes.append(sha256_hash)
        else:
            print("[-] Directory not found!")
        return hashes