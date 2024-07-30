import hashlib
import bcrypt
import os
import itertools
import string
import yaml
import os
import os.path
from pathlib import Path
print(Path.cwd())
yaml_path= str(Path.cwd())+"\\"+"setup.yaml"
print(yaml_path)
with open(yaml_path, 'r') as file:
      machineDetail = yaml.safe_load(file)

print(machineDetail['Admin'])


def hash_passwordd(password):
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256(password_bytes)
    # Get the hexadecimal representation of the hash
    hashed_password = hash_object.hexdigest()
    return hashed_password

# Function to compute the SHA-256 hash of a given password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Brute-force search for the password
def brute_force_search(target_hash, charset, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt_password = ''.join(attempt)
            attempt_hash = hash_password(attempt_password)
            if attempt_hash == target_hash:
                return attempt_password
    return None

# Define the target hash
password = machineDetail['Admin']
target_hash = hash_passwordd(password)

# Define the character set to use for generating passwords
charset = string.ascii_uppercase + string.ascii_lowercase + string.digits +string.punctuation  # a-z and 0-9

# Define the maximum length of passwords to try
max_length = 6

print(f'Password : {password}')
print(f'hash_passwordd : {target_hash}')

# Perform the brute-force search
found_password = brute_force_search(target_hash, charset, max_length)
if found_password:
    print(f'Password found: {found_password}')
else:
    print('Password not found')

