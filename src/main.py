import numpy as np
import sys

from file_reader import FileReader
from matrix import Matrix

if len(sys.argv) < 2 or sys.argv[1] != 'encrypt' and sys.argv[1] != 'decrypt':
    print(sys.argv[1])
    raise ValueError('The second parameter has to be "encrypt" or "decrypt"')

if sys.argv[1] == 'encrypt':
    input_file = FileReader.PLAINTEXT_FILEPATH
    output_file = FileReader.CIPHERTEXT_FILEPATH

elif sys.argv[1] == 'decrypt':
    input_file = FileReader.CIPHERTEXT_FILEPATH
    output_file = FileReader.PLAINTEXT_FILEPATH

# Read the inputted message
input_message = FileReader.read_message_file(input_file)

# Read the key
key_matrix = FileReader.read_key_file()

# Turn the encrypted message into a matrix of Unicode codepoints
unicode_matrix = Matrix.str_to_matrix(input_message, len(key_matrix[0]))

output_matrix = Matrix.multiply_matrices(
    unicode_matrix, 
    key_matrix if sys.argv[1] == 'encrypt' else np.linalg.inv(key_matrix)
)

# Turn the encrypted numbers into Unicode and join it into a str
output_message = Matrix.matrix_to_str(output_matrix)

if sys.argv[1] == 'encrypt':
    print(f'Plaintext message: \n{input_message}')
    print(f'\nKey matrix: \n{key_matrix}')
    print(f'\nCiphertext message: \n{output_message}')
  
elif sys.argv[1] == 'decrypt':
    print(f'Ciphertext message: \n{input_message}')
    print(f'\nKey matrix: \n{key_matrix}')
    print(f'\nPlaintext message: \n{output_message}')

# Write the output into the corresponding file
with open(output_file, 'w', encoding='utf-8') as write_file:
    write_file.write(output_message)