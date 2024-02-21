#!usr/bin/env python3
# coding:utf-8

import subprocess

def main():
    # Appel du script scan_yara.py
    subprocess.run(["python", "modules/yara/scan_yara.py"])

if __name__ == "__main__":
    main()