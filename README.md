# Station-blanche

## How it work?


## Installation:

```sh
git clone https://github.com/Networkion/Station-blanche
cd Station-blanche
pip install -r requirements.txt
```

## Detection:

- hashTable (thanks to VX-Underground to provide us 40M hashs)
- Fonction parsing with lief lib (Thanks to @deadc0de for pointing it out to us)

-----
# PDF generation: 

-> A pdf is created on demand by pypdf including the following information:

- hashfile (sha256 + md5)
- filename
- path
- type file
- PID
- Size