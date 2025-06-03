from PyPDF2 import PdfReader, PdfWriter
import sys


def encrypt_file():
    file_path = input("[+] Enter a file path: ")
    password = input("[+] Enter a password: ")
    encrypted_file_name = input("[+] Enter a name for encrypted file: ")

    writer = PdfWriter()

    try:
        reader = PdfReader(file_path)
    except FileNotFoundError:
        print(f"No file with path {file_path}")
        sys.exit()
            
    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    with open(encrypted_file_name, 'wb') as file:
        writer.write(file)

    print(f"[+] File '{file_path}' was encrypted successfully as '{encrypted_file_name}'")


def decrypt_file():
    file_path = input("[+] Enter a file path: ")
    password = input("[+] Enter a password: ")
    decrypted_file_name = input("[+] Enter a name for decrypted file: ")

    writer = PdfWriter()

    try:
        reader = PdfReader(file_path)
    except FileNotFoundError:
        print(f"No file with path {file_path}")
        sys.exit()

    if reader.is_encrypted:
        reader.decrypt(password)

    for page in reader.pages:
        writer.add_page(page)


    with open(decrypted_file_name, 'wb') as file:
        writer.write(file)

    print(f"[+] File '{file_path}' was decrypted successfully as '{decrypted_file_name}'")

def main():
    choose = input('[+] Enter 0 to encrypt the file, 1 to decrypt: ')
    encrypt_file() if choose == '0' else decrypt_file() 

if __name__ == "__main__":
    main()
