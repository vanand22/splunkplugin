import os
import subprocess  # CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
import hashlib

# Vulnerability: Hardcoded sensitive information
# CWE-798: Use of Hard-coded Credentials
PASSWORD = "SuperSecretPassword"

def run_command(user_input):
    # Vulnerability: OS Command Injection
    # CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
    command = "echo " + user_input
    subprocess.call(command, shell=True)

def hash_password(password):
    # Vulnerability: Use of a weak cryptographic hash function
    # CWE-327: Use of a Broken or Risky Cryptographic Algorithm
    return hashlib.md5(password.encode()).hexdigest()

def main():
    user_input = input("Enter a command to run: ")
    run_command(user_input)

    hashed_password = hash_password(PASSWORD)
    print(f"Hashed password: {hashed_password}")

if __name__ == "__main__":
    main()
