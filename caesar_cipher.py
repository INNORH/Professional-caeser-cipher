"""
Professional Caesar Cipher Implementation

This module provides a robust implementation of the Caesar cipher with support for
encryption, decryption, and brute force attacks. It handles both uppercase and
lowercase letters while preserving non-alphabetic characters.

Author: Professional Implementation
License: MIT
"""

import string
from typing import Union, List, Tuple


class CaesarCipher:
    """
    A professional implementation of the Caesar cipher algorithm.
    
    The Caesar cipher is a substitution cipher where each letter in the plaintext
    is shifted a certain number of places down or up the alphabet.
    """
    
    def __init__(self):
        """Initialize the Caesar cipher with alphabet constants."""
        self.lowercase_letters = string.ascii_lowercase
        self.uppercase_letters = string.ascii_uppercase
        self.alphabet_size = 26
    
    def encrypt(self, text: str, shift: int) -> str:
        """
        Encrypt text using Caesar cipher with the given shift value.
        
        Args:
            text (str): The plaintext to encrypt
            shift (int): The number of positions to shift (positive for right shift)
            
        Returns:
            str: The encrypted ciphertext
            
        Example:
            >>> cipher = CaesarCipher()
            >>> cipher.encrypt("Hello World", 3)
            'Khoor Zruog'
        """
        if not isinstance(text, str):
            raise TypeError("Text must be a string")
        
        if not isinstance(shift, int):
            raise TypeError("Shift must be an integer")
        
        # Normalize shift to be within 0-25 range
        shift = shift % self.alphabet_size
        
        encrypted_text = []
        
        for char in text:
            if char in self.lowercase_letters:
                # Handle lowercase letters
                old_index = self.lowercase_letters.index(char)
                new_index = (old_index + shift) % self.alphabet_size
                encrypted_text.append(self.lowercase_letters[new_index])
            elif char in self.uppercase_letters:
                # Handle uppercase letters
                old_index = self.uppercase_letters.index(char)
                new_index = (old_index + shift) % self.alphabet_size
                encrypted_text.append(self.uppercase_letters[new_index])
            else:
                # Keep non-alphabetic characters unchanged
                encrypted_text.append(char)
        
        return ''.join(encrypted_text)
    
    def decrypt(self, ciphertext: str, shift: int) -> str:
        """
        Decrypt ciphertext using Caesar cipher with the given shift value.
        
        Args:
            ciphertext (str): The ciphertext to decrypt
            shift (int): The shift value used for encryption
            
        Returns:
            str: The decrypted plaintext
            
        Example:
            >>> cipher = CaesarCipher()
            >>> cipher.decrypt("Khoor Zruog", 3)
            'Hello World'
        """
        # Decryption is encryption with negative shift
        return self.encrypt(ciphertext, -shift)
    
    def brute_force(self, ciphertext: str) -> List[Tuple[int, str]]:
        """
        Perform brute force attack on ciphertext by trying all possible shifts.
        
        Args:
            ciphertext (str): The ciphertext to attack
            
        Returns:
            List[Tuple[int, str]]: List of (shift, decrypted_text) tuples
            
        Example:
            >>> cipher = CaesarCipher()
            >>> results = cipher.brute_force("Khoor")
            >>> print(results[3])  # Should show the correct decryption
            (3, 'Hello')
        """
        if not isinstance(ciphertext, str):
            raise TypeError("Ciphertext must be a string")
        
        results = []
        
        for shift in range(self.alphabet_size):
            decrypted = self.decrypt(ciphertext, shift)
            results.append((shift, decrypted))
        
        return results
    
    def is_valid_shift(self, shift: Union[int, str]) -> bool:
        """
        Validate if the shift value is acceptable.
        
        Args:
            shift (Union[int, str]): The shift value to validate
            
        Returns:
            bool: True if shift is valid, False otherwise
        """
        try:
            shift_int = int(shift)
            return True
        except (ValueError, TypeError):
            return False
    
    def analyze_frequency(self, text: str) -> dict:
        """
        Analyze letter frequency in the given text.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Dictionary with letter frequencies
        """
        frequency = {}
        total_letters = 0
        
        for char in text.lower():
            if char in self.lowercase_letters:
                frequency[char] = frequency.get(char, 0) + 1
                total_letters += 1
        
        # Convert to percentages
        for letter in frequency:
            frequency[letter] = (frequency[letter] / total_letters) * 100
        
        return frequency


def main():
    """
    Demonstration function showing basic usage of the Caesar cipher.
    """
    cipher = CaesarCipher()
    
    # Example usage
    original_text = "Hello, World! This is a Caesar Cipher demonstration."
    shift_value = 7
    
    print("=== Caesar Cipher Demonstration ===")
    print(f"Original text: {original_text}")
    print(f"Shift value: {shift_value}")
    
    # Encrypt
    encrypted = cipher.encrypt(original_text, shift_value)
    print(f"Encrypted: {encrypted}")
    
    # Decrypt
    decrypted = cipher.decrypt(encrypted, shift_value)
    print(f"Decrypted: {decrypted}")
    
    # Verify
    print(f"Verification: {original_text == decrypted}")
    
    print("\n=== Brute Force Attack Demo ===")
    test_cipher = "Uryyb, Jbeyq!"
    print(f"Attacking: {test_cipher}")
    
    results = cipher.brute_force(test_cipher)
    for shift, result in results:
        print(f"Shift {shift:2d}: {result}")


if __name__ == "__main__":
    main()
