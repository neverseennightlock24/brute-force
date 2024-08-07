import itertools
import string
import time
import sys
import psutil

class PasswordValidator:
    def __init__(self, password, min_length=1, max_length=3):
        self.password = password
        self.min_length = min_length
        self.max_length = max_length
        self.valid_characters = string.ascii_lowercase + string.digits

    def is_valid(self):
        # Check if the password length is within the allowed range
        if len(self.password) < self.min_length or len(self.password) > self.max_length:
            return False
        
        # Check if all characters in the password are valid
        for char in self.password:
            if char not in self.valid_characters:
                return False
        
        return True

def hacker_print(text, delay=0.017):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def brute_force(target_password):
    # Define the characters to use in the brute force attack
    characters = string.ascii_lowercase + string.digits  # lowercase letters and digits

    # Start time
    start_time = time.time()

    # Hacker-style introduction
    hacker_print("Initializing brute force attack...\n", delay=0.033)
    hacker_print("Characters set: " + characters + "\n", delay=0.033)
    hacker_print(f"Target password length range: 1 to 3 characters\n", delay=0.033)
    hacker_print("Starting attack...\n", delay=0.033)
    
    # Iterate through all possible lengths of the password
    for password_length in range(1, 4):  # Let's limit to 3 characters for this example
        # Generate all possible combinations of the given length
        for attempt in itertools.product(characters, repeat=password_length):
            # Join the tuple of characters into a string
            attempt = ''.join(attempt)
            
            # Print the current attempt (optional)
            hacker_print(f"Trying: {attempt}", delay=0.0067)
            
            # Display current RAM usage
            ram_usage = psutil.virtual_memory().percent
            hacker_print(f"Current RAM usage: {ram_usage}%", delay=0.0067)
            
            # Check if the attempt matches the target password
            if attempt == target_password:
                # End time
                end_time = time.time()
                
                hacker_print(f"\nPassword found: {attempt}", delay=0.033)
                hacker_print(f"Time taken: {end_time - start_time:.2f} seconds", delay=0.033)
                return attempt

    hacker_print("Password not found within the given length limit.", delay=0.033)
    return None

def get_password_from_user():
    while True:
        password = input("Enter a password to brute force (1-3 characters, lowercase letters and digits only): ")
        validator = PasswordValidator(password)
        if validator.is_valid():
            return password
        else:
            print("Invalid password! Please enter a valid password (1-3 characters, lowercase letters and digits only).")

# Example usage
target_password = get_password_from_user()
found_password = brute_force(target_password)
