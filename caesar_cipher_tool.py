import pyfiglet
from termcolor import colored

# Function to encrypt using Caesar Cipher
def caesar_encrypt(plaintext, shift):
    encrypted_text = ''
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt using Caesar Cipher
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text

# ASCII Banner
def print_banner():
    banner = pyfiglet.figlet_format("Cipher Toolkit", font="slant")  # You can change font here
    print(colored(banner, "cyan"))
    print(colored("Developed by n4it40_07", "yellow"))
    print("=" * 60)

# Caesar Brute-force Mode
def brute_force_mode(text):
    print(colored("Brute Force Results (All 26 Shifts):", "magenta"))
    print("-" * 50)
    for shift in range(0, 26):  # Include shift 0
        result = caesar_decrypt(text, shift)
        print(colored(f"Shift {str(shift).rjust(2)}: ", "yellow") + colored(result, "blue"))

# Main Menu
def main():
    while True:
        print_banner()
        print(colored("Choose an option:", "green"))
        print(colored("[1] Encrypt", "cyan"))
        print(colored("[2] Decrypt", "cyan"))
        print(colored("[3] Brute Force Decryption", "cyan"))
        print(colored("[4] Exit", "red"))

        choice = input(colored("Enter your choice: ", "yellow")).strip()

        if choice == '1':
            text = input(colored("Enter plaintext to encrypt: ", "green"))
            shift = int(input(colored("Enter shift (0-25): ", "green")))
            result = caesar_encrypt(text, shift)
            print(colored("Encrypted Text:", "magenta"), colored(result, "blue"))
        elif choice == '2':
            text = input(colored("Enter ciphertext to decrypt: ", "green"))
            shift = int(input(colored("Enter shift (0-25): ", "green")))
            result = caesar_decrypt(text, shift)
            print(colored("Decrypted Text:", "magenta"), colored(result, "blue"))
        elif choice == '3':
            text = input(colored("Enter ciphertext for brute force: ", "green"))
            brute_force_mode(text)
        elif choice == '4':
            print(colored("Exiting... Thank you for using Cipher Toolkit!", "red"))
            break
        else:
            print(colored("Invalid choice. Please try again.", "red"))

        input(colored("\nPress Enter to continue...", "white"))

if __name__ == "__main__":
    main()
