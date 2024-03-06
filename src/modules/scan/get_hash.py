#!/usr/bin/env python3
# coding:utf-8

import hashlib
import os
from typing import List


class FileHash(object):
    BUF_SIZE: int = 4096

    @staticmethod
    def get_hash(path: str, BUF_SIZE=BUF_SIZE) -> str:
        """
           Get hash for a single file
        """
        hash_value = hashlib.sha256()
        with open(path, "rb") as file:
            for byte_block in iter(lambda: file.read(BUF_SIZE), b""):
                hash_value.update(byte_block)
        return hash_value.hexdigest()

    def get_file_hashes(self, directory: str) -> List[str]:
        """
          Get SHA-256 hashes of files in a directory
        """
        if not os.path.isdir(directory):
            raise ValueError(f"{directory} is not a valid directory")

        return [self.get_hash(os.path.join(directory, x)) for x in os.listdir(directory)]
