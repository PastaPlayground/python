from cryptography.fernet import Fernet


def encrypt(filename, key):
    # get encryption key
    encryption_key = Fernet(key)

    # open and read file using bytes for encryption
    with open(filename, "rb") as file:
        contents = file.read()

    # encrypt contents
    encrypted_data = encryption_key.encrypt(contents)

    # write encrypted contents back to file
    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
