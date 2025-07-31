# Professional Caesar Cipher

A comprehensive and professional implementation of the Caesar cipher in Python, featuring encryption, decryption, brute force attacks, and frequency analysis.

## Features

- **Encryption & Decryption**: Robust Caesar cipher implementation with proper handling of case sensitivity
- **Brute Force Attack**: Automatically try all possible shifts to crack encrypted text
- **Frequency Analysis**: Analyze letter frequency distribution in text
- **Command Line Interface**: Both interactive and command-line modes
- **Comprehensive Testing**: Full unit test suite with edge case coverage
- **Professional Code**: Well-documented, type-hinted, and following Python best practices

## Installation

1. Clone this repository:
```bash
git clone (https://github.com/INNORH/Professional-caeser-cipher.git)
cd professional-caesar-cipher
```

2. No additional dependencies required - uses only Python standard library!

## Usage

### Command Line Interface

#### Interactive Mode
```bash
python cli.py
# or
python cli.py --interactive
```

#### Direct Commands
```bash
# Encrypt text
python cli.py --encrypt "Hello World" --shift 3

# Decrypt text
python cli.py --decrypt "Khoor Zruog" --shift 3

# Brute force attack
python cli.py --brute-force "Khoor Zruog"

# Frequency analysis
python cli.py --frequency "This is sample text for analysis"
```

### Python Module Usage

```python
from caesar_cipher import CaesarCipher

# Create cipher instance
cipher = CaesarCipher()

# Encrypt text
encrypted = cipher.encrypt("Hello World", 3)
print(encrypted)  # Output: "Khoor Zruog"

# Decrypt text
decrypted = cipher.decrypt("Khoor Zruog", 3)
print(decrypted)  # Output: "Hello World"

# Brute force attack
results = cipher.brute_force("Khoor Zruog")
for shift, text in results:
    print(f"Shift {shift}: {text}")

# Frequency analysis
frequencies = cipher.analyze_frequency("Hello World")
print(frequencies)
```

## API Reference

### CaesarCipher Class

#### Methods

- `encrypt(text: str, shift: int) -> str`
  - Encrypts text using Caesar cipher with given shift
  - Preserves case and non-alphabetic characters

- `decrypt(ciphertext: str, shift: int) -> str`
  - Decrypts ciphertext using Caesar cipher with given shift
  - Equivalent to encrypting with negative shift

- `brute_force(ciphertext: str) -> List[Tuple[int, str]]`
  - Attempts all possible shifts (0-25) on ciphertext
  - Returns list of (shift, decrypted_text) tuples

- `analyze_frequency(text: str) -> dict`
  - Analyzes letter frequency in text
  - Returns dictionary with letter frequencies as percentages

- `is_valid_shift(shift: Union[int, str]) -> bool`
  - Validates if shift value is acceptable
  - Returns True if shift can be converted to integer

## Examples

### Basic Encryption/Decryption
```python
cipher = CaesarCipher()

# Encrypt a message
message = "Meet me at midnight!"
encrypted = cipher.encrypt(message, 13)
print(f"Encrypted: {encrypted}")
# Output: "Zrrg zr ng zvqavtug!"

# Decrypt the message
decrypted = cipher.decrypt(encrypted, 13)
print(f"Decrypted: {decrypted}")
# Output: "Meet me at midnight!"
```

### Brute Force Attack
```python
cipher = CaesarCipher()

# Unknown ciphertext
mystery_text = "Wkh txlfn eurzq ira"

# Try all possible shifts
results = cipher.brute_force(mystery_text)

# Look for meaningful English text
for shift, text in results:
    print(f"Shift {shift:2d}: {text}")
    
# Shift  3: The quick brown fox
```

### Frequency Analysis
```python
cipher = CaesarCipher()

text = "The quick brown fox jumps over the lazy dog"
frequencies = cipher.analyze_frequency(text)

# Sort by frequency
sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

for letter, freq in sorted_freq:
    print(f"{letter.upper()}: {freq:5.1f}%")
```

## Testing

Run the comprehensive test suite:

```bash
python test_caesar_cipher.py
```

The test suite includes:
- Basic encryption/decryption tests
- Edge cases (empty strings, large shifts, unicode)
- Brute force attack validation
- Frequency analysis verification
- Type error handling
- Round-trip testing (encrypt → decrypt → original)

## File Structure

```
professional-caesar-cipher/
├── caesar_cipher.py      # Main cipher implementation
├── cli.py               # Command line interface
├── test_caesar_cipher.py # Unit tests
├── README.md            # This documentation
├── requirements.txt     # Python dependencies (empty - stdlib only)
├── .gitignore          # Git ignore file
└── LICENSE             # MIT License
```

## Algorithm Details

The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 3:

- A → D
- B → E  
- C → F
- ...
- X → A (wraps around)
- Y → B
- Z → C

### Key Features of This Implementation:

1. **Case Preservation**: Uppercase letters remain uppercase, lowercase remain lowercase
2. **Non-alphabetic Preservation**: Numbers, punctuation, and spaces are unchanged
3. **Wrap-around**: Properly handles alphabet boundaries (Z+1 = A)
4. **Shift Normalization**: Large shifts are reduced modulo 26
5. **Bidirectional**: Same algorithm for encryption and decryption (with negative shift)

## Security Note

⚠️ **Educational Purpose Only**: The Caesar cipher is cryptographically weak and should never be used for actual security purposes. It can be easily broken with frequency analysis or brute force attacks. This implementation is for educational and demonstration purposes only.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Professional Implementation for Educational Purposes

## Acknowledgments

- Caesar cipher algorithm attributed to Julius Caesar
- Implementation follows Python best practices and PEP 8 style guide
- Comprehensive testing ensures reliability and correctness
