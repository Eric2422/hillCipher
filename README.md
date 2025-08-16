# Hill Cipher
Encrypts and decrypts messages using Hill cipher.

## Usage
Both the plaintext and ciphertext can contain any character represented by Unicode.
The plaintext is stored as a string in `input_output/plaintext.txt`.
The ciphertext is stored as a string in `input_output/ciphertext.txt`.
The key is a CSV of integers stored in `input_output/key.csv`.

### Encrypting
Enter the plaintext into `input_output/ciphertext.txt`.
The messages can contain any character that is included in Unicode.
Enter an invertible matrix into `input_output/key.csv`.
Type `python src/main.py encrypt`

### Decrypting
Enter the ciphertext into `input_output/ciphertext.txt`.
The messages can contain any character that is included in Unicode.
Enter an invertible matrix into `input_output/key.csv`.
Type `python src/main.py decrypt`
