#!usr/bin/env python3.11
#coding:utf-8

import hashlib
import pypdf
from pathlib import Path

class Detection:

    def hashSum(file):
        file_content = open(file).read().encode()
        return hashFile = hashlib.sha256(file_content).hexdigest()


    def checkFile(file):
        with open ("hash.txt", "r") as hashList, (file,"r") as malware:
            if hashsum in hash.txt == hashsum in malware:
                print("Malware detected")
            else:
                print("Take care but nothing is wrong")

    def convertPdf():
    
    def main():

if __name__ == "__main__"
    main()