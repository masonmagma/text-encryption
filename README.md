python CLI message encryption/decryption module

Hello and welcome to the README.md file of my text encryption/decryption module.

- This project uses pythons built in cryptography module to allow a user to generate and use a key to either encrypt or decrypt a secret message.
- This message can only be decrypted by being able to supply the correct key cipher to obtain the orginal plaintext message originally encrypted.

Install requirements
- Using this module requires pip and pythons cryptography module which may not be installed automatically.

Install pip
- to install pip perform the following command in visual studios code terminal or powershell: python -m ensurepip --default-pip

You can also install pip from the python installer here --> https://www.python.org/downloads/
when going through the python install wizard make sure to check the box "Add Python to PATH"

Installing the cryptography module
-perform the 2 following commands in visual studio code terminal or powershell: 

- pip install cryptography
- pip install --upgrade cryptography

Module Usage

- This script secret_message.py can be imported as a module into another script or ran by itself to encrypt and decrypt messages.

- To run this script on its own use powershell and navigate to the directory you have the .py script saved in:
ex: cd .\Desktop\python_scripts\

- To run the python script and access the CLI interface use the following command:
python .\secret_message.py

The script will then prompt you if you want to create a new key or enter your own:
-respond with "y" or "n" and hit enter to confirm your choice

-When you generate a new key make sure to copy it with ctrl+c and save it somewhere safe. This is important for later decrypting messages you encrypt with that secret key.


