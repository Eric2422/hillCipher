import numpy as np
import sys

from file_reader import FileReader

def str_to_matrix(message: str, num_cols: int):
    """
    Convert a str into a 2D matrix with num_cols number of columns.
    Any spaces at the end are padded with 0s.

    Parameters
    ----------
    message : str
        A string representing the message.
    num_cols : int
        The number of columns the 2D matrix has. 

    Returns
    -------
    np.array
        A 2D matrix represented by a numpy array.
        It has num_cols number of cols.
    """
    # Convert the message into an array of Unicdoe codepoints
    unicode_array = np.array([ord(num) for num in message])

    # If the message does not fit into the array
    if len(unicode_array) % num_cols != 0:
        # Pad it with as many 0s as necessary
        unicode_array = np.append(unicode_array, [0 for i in range(num_cols - len(unicode_array) % num_cols)])

    # Reshape the unicode message into a 2D array with cols number of columns
    #   and as many rows as necessary 
    return np.reshape(unicode_array, (-1, num_cols))


def matrix_to_str(matrix: np.array) -> str:
    """
    Converts a 2D matrix of Unicode codepoints into a string

    Parameters
    ----------
    matrix : np.array
        A 2D matrix containing Unicode codepoints

    Returns
    -------
    str
        The str encoded by the Unicode codepoints
    """
    return ''.join([chr(round(unicode)) for unicode in matrix.flatten().tolist()])


def multiply_matrices(message_matrix: np.array, key_matrix: np.array) -> np.array:
    return np.matmul(message_matrix, key_matrix) % sys.maxunicode


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
unicode_matrix = str_to_matrix(input_message, len(key_matrix[0]))

output_matrix = multiply_matrices(
    unicode_matrix, 
    key_matrix if sys.argv[1] == 'encrypt' else np.linalg.inv(key_matrix)
)

# Turn the encrypted numbers into Unicode and join it into a str
output_message = matrix_to_str(output_matrix)

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