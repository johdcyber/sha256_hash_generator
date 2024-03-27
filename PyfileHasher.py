import hashlib
import sys


def hash_file(filepath):
    """This function returns the SHA-256 hash
    of the file passed into it."""

    # make a hash object
    h = hashlib.sha256()

    # open file for reading in binary mode
    with open(filepath, 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    hash_result = hash_file(file_path)
    print(f"The SHA-256 hash of the file is: {hash_result}")
