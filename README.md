# Overview
Encrypts and decrypts messages using Hill cipher

# Guide
Both the encrypted and decrypted message can contain any character represented by Unicode.
The decrypted message is stored as a string in a input_output/decrypted.txt.
The encrypted message is stored as a series of integers separated by spaces in input_output/encrypted.txt.
The key is a CSV of integers stored in input_output/key.csv.

## Encrypting
Enter an unencrypted message into unencrypted.txt
The messages can contain any character that is included in Unicode.
Enter an invertible matrix into key.csv.
