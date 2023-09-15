#!usr/bin/env python3.11
#coding:utf-8

import lief, hashlib, pypdf

class Detection:
    
    def  __init__(self):
        self.file = file

    # Check the file hash in SHA-256
    def hashSum(self):
        file_content = open(self.file).read().encode()
        return hashFile = hashlib.sha256(file_content).hexdigest()

    # Check if the hash match with the hashTable
    def checkFile(self):
        with open ("hashes.txt", "r") as hashList, (self.file,"r") as malware:
            if hashsum in hashes.txt == hashsum in malware:
                print("Malware detected")
            else:
                print("Take care but nothing is wrong")


    def parseFile(self):
        binary = self.file
        
    # Create a PDF
    def convertPdf():
        # Create a pdf with pyPDF
        # Name of the file
        # path system
        # taille
        # headers
        # 

    def main():

if __name__ == "__main__"
    main()