import itertools
import string
import time
import sys
import psutil

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
    hacker_print("Target password length range: 1 to 3 characters\n", delay=0.033)
    hacker_print("Starting attack...\n", delay=0.033)
    
    # Iterate through all possible lengths of the password
    for password_length in range(1, 3):  # Let's limit to 3 characters for this example
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

# Example usage
target_password = "ab3"
found_password = brute_force(target_password)
