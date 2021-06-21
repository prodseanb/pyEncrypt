# pyEncrypt
[![Generic badge](https://img.shields.io/badge/fork-🔱-<COLOR>.svg)](https://github.com/prodseanb/pyEncrypt/fork)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/prodseanb/pyEncrypt/blob/master/LICENSE)
[![Generic badge](https://img.shields.io/badge/follow-LinkedIn-<COLOR>.svg)](https://www.linkedin.com/in/sean-bachiller-40b63417b/)
[![Generic badge](https://img.shields.io/badge/follow-Twitter-<COLOR>.svg)](https://twitter.com/prodseanb)
[![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://github.com/prodseanb/pyEncrypt/blob/master/run.py)
<br />
```
────────────────████
───────────────█░░███
───────────────█░░████
────────────────███▒██─────████████
──────████████─────█▒█──████▒▒▒▒▒▒████
────███▒▒▒▒▒▒████████████░░████▒▒▒▒▒███
──██▒▒▒▒░▒▒████░░██░░░░██░░░░░█▒▒▒▒▒▒▒███
─██▒▒░░░░▒██░░░░░█▒░░░░░██▒░░░░░░░▒▒▒▒▒▒█
██▒░░░░░▒░░░░░░░░░▒░░░░░░░▒▒░░░░░░░▒▒▒▒▒██
█░░░░░░▒░░░██░░░░░░░░░░░░░██░░░░░░░░▒▒▒▒▒█
█░░░░░░░░█▒▒███░░░░░░░░░█▒▒███░░░░░░░▒▒▒▒█
█░░░░░░░████████░░░░░░░████████░░░░░░▒▒▒▒█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█
██░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░▒▒▒▒█
─█░░░░██░█░░░░░░░░░░░░░░░░░░░░░░░███▒▒▒▒▒█
─█▒▒░░░░█████░░░█░░░░██░░░██░░████░▒▒▒▒▒▒█
─██▒▒░░░░░█████████████████████░░░▒▒▒▒▒▒██
──██▒▒▒▒░░░░░██░░░███░░░██░░░█░░░▒▒▒▒▒▒██
───███▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█████
─────███▒▒▒▒▒▒░░░░░░░░░░░░░▒▒▒▒▒▒████
────────██████████████████████████
────╔═╗──────────╔╗
╔═╦╦╣╦╬═╦╦═╦╦╦╦╦═╣╚╗
║╬║║║╩╣║║║═╣╔╣║║╬║╔╣
║╔╬╗╠═╩╩═╩═╩╝╠╗║╔╩═╝
╚╝╚═╝────────╚═╩╝                                                                         
 *      v1.2
 *      @Author: prodseanb
 *      @GitHub: https://github.com/prodseanb/pyEncrypt 
 *
 *
```

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) <br />

## Objective
The objective of this program is to take data input and encrypt it in one the following hashing/encoding methods:
- aes
- md5
- sha256
- rot13
- caesar cipher
- hex
- base64

## Usage
To run this project:
### Clone repo 
```bash
git clone https://github.com/prodseanb/pyEncrypt.git
```
### Install requirements and execute
```bash
pip3 install -r requirements.txt
python3 run.py [option]
```
### Documentation
```
pyEncrypt - Data encryption. v1.2 (https://github.com/prodseanb/pyEncrypt)
Usage: 
	python3 run.py [option]
	Only one parameter is required.
        -h / --help: Display this documentation.
	--aes: AES encryption
	--md5: MD5 hash
	--sha256: SHA256 hash
	--rot13: ROT13 encryption
	--caesar: Caesar Cipher encryption
	--hex: Encode in Hex
	--base64: Encode in Base64
Examples:
	Try executing these examples.
	python3 run.py --md5
	python3 run.py --sha256
	python3 run.py --base64
```
### Run on Docker
```bash
sudo docker pull prodseanb/pyencrypt
sudo docker run -t -i prodseanb/pyencrypt [option]
```

### License
[MIT License](https://github.com/prodseanb/Encryption/blob/master/LICENSE)


Copyright (c) 2021 Sean Bachiller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
