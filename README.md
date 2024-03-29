# Station-blanche

## How it works?

- Detection with HashTable (SHA-256), Yara rules and a Antivirus :p
  Give a path and the app scan & detect.

## Pre-requisites:

- Docker
- Python3

## Installation:

```sh
git clone https://github.com/Networkion/Station-blanche
cd Station-blanche
pip install -r requirements.txt
docker compose up -d
python /src/database/import_hash.py
```

## Detection:

- hashTable (thanks to VX-Underground, Malware Bazaar (CERT-PL) to provide us hashes)
- Yara rules (Thanks to Cyb3r0ps) => Scan only .exe

-----

# How to use ?

```ssh
python3 main.py -f [file] -d [directory] --scan --yara
python3 main.py --file [file] --dir [directory] --scan --yara 
```
