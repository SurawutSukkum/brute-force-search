import hashlib
import bcrypt
def brute_force_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
arr = [3, 5, 1, 4, 2]
target = 4
index = brute_force_search(arr, target)
print(f"Element {target} found at index {index}" if index != -1 else "Element not found")

def hash_password(password):
    # Create a new sha256 hash object
    hash_obj = hashlib.sha256()
    # Update the hash object with the password encoded as bytes
    hash_obj.update(password.encode('utf-8'))
    # Return the hexadecimal representation of the digest
    return hash_obj.hexdigest()


def hash_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def check_password(hashed_password, user_password):
    # Check the hashed password against the user's password
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

# Example usage1
password = "Test"
print(f"Password: {password}")
hashed_password = hash_password(password)
print(f"Hashed password: {hashed_password.decode()}")
is_correct = check_password(hashed_password, password)
print(f"Password is correct: {is_correct}")



