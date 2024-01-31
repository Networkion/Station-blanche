#!/usr/bin/env python3.11
# coding:utf-8
# author: Isis

import hashlib
import os
from typing import List

class calculHash:

    # Const
    BUF_SIZE: int = 65534

    @staticmethod
    # Get SHA-256 hash of a file
    def getHashFile(file_path: str) -> str:
        hashFile = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(Detection.BUF_SIZE), b""):
                hashFile.update(byte_block)
        return hashFile.hexdigest()

    @staticmethod
    # Get SHA-256 hash of files in a directory
    def getFilePath(directory_path: str) -> List[str]:
        hashes = []
        if os.path.isdir(directory_path):
            # Iterate over files in the directory
            for file_name in os.listdir(directory_path):
                file_path = os.path.join(directory_path, file_name)
                # Check if the path is a file
                if os.path.isfile(file_path):
                    # Calculate hash for each file
                    sha256_hash = calculHash.getHashFile(file_path)
                    print(f"[+] SHA256 hash of {file_name}: {sha256_hash}")
                    hashes.append(sha256_hash)
        else:
            print("[-] Directory not found !")
        return hashes