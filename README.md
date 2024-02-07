# Station-blanche

## How it works?

- Detection with HashTable (SHA-256), Yara rules and a EDR :p

The application works with a GUI (tkinter). Give a path and the app scan & detect.


## Installation:

```sh
git clone https://github.com/Networkion/Station-blanche
cd Station-blanche
pip install -r requirements.txt
docker compose up -d
```
And have fun :)

## Detection:

- hashTable (thanks to VX-Underground, Malware Bazaar (CERT-PL) to provide us 40M hashes)
- Yara rules
- AV

-----

## PDF generation: 

-> A pdf is created on demand by reportlab including the following information:

- hashfile (sha256)
- filename
- path
- type file
- Size