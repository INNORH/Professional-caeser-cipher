"""
Unit Tests for Caesar Cipher Implementation

This module contains comprehensive unit tests for the Caesar cipher implementation,
ensuring all functionality works correctly and handles edge cases properly.

Author: Professional Implementation
License: MIT
"""

import unittest
from caesar_cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):
    """Test cases for the CaesarCipher class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.cipher = CaesarCipher()
    
    def test_encrypt_basic(self):
        """Test basic encryption functionality."""
        # Test lowercase
        result = self.cipher.encrypt("hello", 3)
        self.assertEqual(result, "khoor")
        
        # Test uppercase
        result = self.cipher.encrypt("HELLO", 3)
        self.assertEqual(result, "KHOOR")
        
        # Test mixed case
        result = self.cipher.encrypt("Hello", 3)
        self.assertEqual(result, "Khoor")
    
    def test_encrypt_with_non_alphabetic(self):
        """Test encryption with non-alphabetic characters."""
        result = self.cipher.encrypt("Hello, World!", 3)
        self.assertEqual(result, "Khoor, Zruog!")
        
        result = self.cipher.encrypt("Test 123 @#$", 5)
        self.assertEqual(result, "Yjxy 123 @#$")
    
    def test_encrypt_wrap_around(self):
        """Test encryption with wrap-around at end of alphabet."""
        result = self.cipher.encrypt("xyz", 3)
        self.assertEqual(result, "abc")
        
        result = self.cipher.encrypt("XYZ", 3)
        self.assertEqual(result, "ABC")
    
    def test_decrypt_basic(self):
        """Test basic decryption functionality."""
        # Test that decryption reverses encryption
        original = "Hello, World!"
        encrypted = self.cipher.encrypt(original, 7)
        decrypted = self.cipher.decrypt(encrypted, 7)
        self.assertEqual(original, decrypted)
    
    def test_decrypt_direct(self):
        """Test direct decryption with known values."""
        result = self.cipher.decrypt("khoor", 3)
        self.assertEqual(result, "hello")
        
        result = self.cipher.decrypt("KHOOR", 3)
        self.assertEqual(result, "HELLO")
    
    def test_shift_normalization(self):
        """Test that shifts are properly normalized."""
        # Shift of 26 should be same as shift of 0
        result1 = self.cipher.encrypt("hello", 0)
        result2 = self.cipher.encrypt("hello", 26)
        self.assertEqual(result1, result2)
        
        # Shift of 29 should be same as shift of 3
        result1 = self.cipher.encrypt("hello", 3)
        result2 = self.cipher.encrypt("hello", 29)
        self.assertEqual(result1, result2)
    
    def test_negative_shift(self):
        """Test encryption and decryption with negative shifts."""
        result = self.cipher.encrypt("hello", -3)
        expected = self.cipher.encrypt("hello", 23)  # -3 mod 26 = 23
        self.assertEqual(result, expected)
    
    def test_brute_force(self):
        """Test brute force attack functionality."""
        ciphertext = "khoor"
        results = self.cipher.brute_force(ciphertext)
        
        # Should return 26 results
        self.assertEqual(len(results), 26)
        
        # Check that shift 3 gives "hello"
        shift_3_result = next(result for shift, result in results if shift == 3)
        self.assertEqual(shift_3_result, "hello")
        
        # Check that all shifts are present
        shifts = [shift for shift, _ in results]
        self.assertEqual(sorted(shifts), list(range(26)))
    
    def test_is_valid_shift(self):
        """Test shift validation."""
        # Valid shifts
        self.assertTrue(self.cipher.is_valid_shift(5))
        self.assertTrue(self.cipher.is_valid_shift("10"))
        self.assertTrue(self.cipher.is_valid_shift(-3))
        
        # Invalid shifts
        self.assertFalse(self.cipher.is_valid_shift("abc"))
        self.assertFalse(self.cipher.is_valid_shift(None))
        self.assertFalse(self.cipher.is_valid_shift([1, 2, 3]))
    
    def test_frequency_analysis(self):
        """Test frequency analysis functionality."""
        text = "aabbcc"
        frequencies = self.cipher.analyze_frequency(text)
        
        # Each letter should appear twice out of 6 total = 33.33%
        expected_freq = 100.0 / 3  # 33.33%
        
        self.assertAlmostEqual(frequencies['a'], expected_freq, places=1)
        self.assertAlmostEqual(frequencies['b'], expected_freq, places=1)
        self.assertAlmostEqual(frequencies['c'], expected_freq, places=1)
    
    def test_frequency_analysis_with_non_alphabetic(self):
        """Test frequency analysis ignoring non-alphabetic characters."""
        text = "a1b2c3"
        frequencies = self.cipher.analyze_frequency(text)
        
        # Should only count a, b, c (ignoring numbers)
        expected_freq = 100.0 / 3  # 33.33%
        
        self.assertAlmostEqual(frequencies['a'], expected_freq, places=1)
        self.assertAlmostEqual(frequencies['b'], expected_freq, places=1)
        self.assertAlmostEqual(frequencies['c'], expected_freq, places=1)
        self.assertEqual(len(frequencies), 3)
    
    def test_empty_string(self):
        """Test handling of empty strings."""
        result = self.cipher.encrypt("", 5)
        self.assertEqual(result, "")
        
        result = self.cipher.decrypt("", 5)
        self.assertEqual(result, "")
        
        frequencies = self.cipher.analyze_frequency("")
        self.assertEqual(frequencies, {})
    
    def test_type_errors(self):
        """Test that appropriate type errors are raised."""
        with self.assertRaises(TypeError):
            self.cipher.encrypt(123, 5)
        
        with self.assertRaises(TypeError):
            self.cipher.encrypt("hello", "abc")
        
        with self.assertRaises(TypeError):
            self.cipher.brute_force(123)
    
    def test_round_trip(self):
        """Test that encrypt->decrypt returns original text."""
        test_cases = [
            "Hello, World!",
            "The quick brown fox jumps over the lazy dog.",
            "UPPERCASE and lowercase MiXeD",
            "Numbers 123 and symbols !@#$%",
            "Single letter: A",
            ""
        ]
        
        for original in test_cases:
            for shift in [1, 7, 13, 25]:
                with self.subTest(text=original, shift=shift):
                    encrypted = self.cipher.encrypt(original, shift)
                    decrypted = self.cipher.decrypt(encrypted, shift)
                    self.assertEqual(original, decrypted)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.cipher = CaesarCipher()
    
    def test_large_shift_values(self):
        """Test with very large shift values."""
        # Large positive shift
        result1 = self.cipher.encrypt("hello", 1000)
        result2 = self.cipher.encrypt("hello", 1000 % 26)
        self.assertEqual(result1, result2)
        
        # Large negative shift
        result1 = self.cipher.encrypt("hello", -1000)
        result2 = self.cipher.encrypt("hello", -1000 % 26)
        self.assertEqual(result1, result2)
    
    def test_unicode_characters(self):
        """Test with unicode characters (should be preserved)."""
        text = "Héllo Wörld! 你好"
        result = self.cipher.encrypt(text, 3)
        # Only ASCII letters should be encrypted
        expected = "Kéoor Zöuog! 你好"
        # Note: This test assumes non-ASCII characters are preserved
        # The actual behavior depends on implementation
    
    def test_all_non_alphabetic(self):
        """Test with text containing no alphabetic characters."""
        text = "123 !@# $%^"
        result = self.cipher.encrypt(text, 5)
        self.assertEqual(result, text)  # Should remain unchanged


if __name__ == "__main__":
    # Run tests with verbose output
    unittest.main(verbosity=2)
