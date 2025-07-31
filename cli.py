#!/usr/bin/env python3
"""
Command Line Interface for Caesar Cipher

This module provides an interactive command-line interface for the Caesar cipher,
allowing users to encrypt, decrypt, and perform brute force attacks on text.

Author: Professional Implementation
License: MIT
"""

import argparse
import sys
from caesar_cipher import CaesarCipher


def interactive_mode():
    """Run the Caesar cipher in interactive mode."""
    cipher = CaesarCipher()
    
    print("=" * 50)
    print("    Professional Caesar Cipher Tool")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Brute force attack")
        print("4. Frequency analysis")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            encrypt_interactive(cipher)
        elif choice == "2":
            decrypt_interactive(cipher)
        elif choice == "3":
            brute_force_interactive(cipher)
        elif choice == "4":
            frequency_analysis_interactive(cipher)
        elif choice == "5":
            print("Thank you for using Caesar Cipher Tool!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


def encrypt_interactive(cipher):
    """Handle interactive encryption."""
    text = input("Enter text to encrypt: ")
    
    while True:
        shift_input = input("Enter shift value (0-25): ")
        if cipher.is_valid_shift(shift_input):
            shift = int(shift_input)
            break
        else:
            print("Invalid shift value. Please enter a number.")
    
    encrypted = cipher.encrypt(text, shift)
    print(f"\nOriginal:  {text}")
    print(f"Encrypted: {encrypted}")


def decrypt_interactive(cipher):
    """Handle interactive decryption."""
    text = input("Enter text to decrypt: ")
    
    while True:
        shift_input = input("Enter shift value (0-25): ")
        if cipher.is_valid_shift(shift_input):
            shift = int(shift_input)
            break
        else:
            print("Invalid shift value. Please enter a number.")
    
    decrypted = cipher.decrypt(text, shift)
    print(f"\nCiphertext: {text}")
    print(f"Decrypted:  {decrypted}")


def brute_force_interactive(cipher):
    """Handle interactive brute force attack."""
    text = input("Enter ciphertext to attack: ")
    
    print(f"\nBrute force results for: {text}")
    print("-" * 40)
    
    results = cipher.brute_force(text)
    for shift, result in results:
        print(f"Shift {shift:2d}: {result}")
    
    print("-" * 40)
    print("Look for meaningful English text above!")


def frequency_analysis_interactive(cipher):
    """Handle interactive frequency analysis."""
    text = input("Enter text for frequency analysis: ")
    
    frequencies = cipher.analyze_frequency(text)
    
    if not frequencies:
        print("No alphabetic characters found in the text.")
        return
    
    print(f"\nFrequency analysis for: {text}")
    print("-" * 30)
    
    # Sort by frequency (descending)
    sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    
    for letter, freq in sorted_freq:
        print(f"{letter.upper()}: {freq:5.1f}%")


def main():
    """Main function with command line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Professional Caesar Cipher Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py --encrypt "Hello World" --shift 3
  python cli.py --decrypt "Khoor Zruog" --shift 3
  python cli.py --brute-force "Khoor Zruog"
  python cli.py --interactive
        """
    )
    
    parser.add_argument(
        "--encrypt", "-e",
        help="Text to encrypt"
    )
    
    parser.add_argument(
        "--decrypt", "-d",
        help="Text to decrypt"
    )
    
    parser.add_argument(
        "--brute-force", "-b",
        help="Text to brute force attack"
    )
    
    parser.add_argument(
        "--shift", "-s",
        type=int,
        help="Shift value for encryption/decryption"
    )
    
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Run in interactive mode"
    )
    
    parser.add_argument(
        "--frequency", "-f",
        help="Perform frequency analysis on text"
    )
    
    args = parser.parse_args()
    
    cipher = CaesarCipher()
    
    # If no arguments provided, run interactive mode
    if len(sys.argv) == 1:
        interactive_mode()
        return
    
    if args.interactive:
        interactive_mode()
        return
    
    if args.encrypt:
        if args.shift is None:
            print("Error: --shift is required for encryption")
            sys.exit(1)
        
        result = cipher.encrypt(args.encrypt, args.shift)
        print(f"Original:  {args.encrypt}")
        print(f"Encrypted: {result}")
    
    elif args.decrypt:
        if args.shift is None:
            print("Error: --shift is required for decryption")
            sys.exit(1)
        
        result = cipher.decrypt(args.decrypt, args.shift)
        print(f"Ciphertext: {args.decrypt}")
        print(f"Decrypted:  {result}")
    
    elif args.brute_force:
        print(f"Brute force attack on: {args.brute_force}")
        print("-" * 40)
        
        results = cipher.brute_force(args.brute_force)
        for shift, result in results:
            print(f"Shift {shift:2d}: {result}")
    
    elif args.frequency:
        frequencies = cipher.analyze_frequency(args.frequency)
        
        if not frequencies:
            print("No alphabetic characters found in the text.")
            return
        
        print(f"Frequency analysis for: {args.frequency}")
        print("-" * 30)
        
        sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        for letter, freq in sorted_freq:
            print(f"{letter.upper()}: {freq:5.1f}%")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
