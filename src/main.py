import numpy as np
import sys

from file_reader import FileReader

def create_2d_matrix(array: np.array, num_cols: int):
    """
    Convert a 1D array into a 2D matrix with num_cols number of columns.
    Any spaces at the end are padded with 0s.

    Parameters
    ----------
    array : np.array
        A 1D numpy array.
    num_cols : int
        The number of columns the 2D matrix has. 

    Returns
    -------
    np.array
        A 2D matrix represented by a numpy array.
        It has num_cols number of cols.
    """
    # If the message does not fit into the array
    if len(array) % num_cols != 0:
        # Pad it with as many 0s as necessary
        array = np.append(array, [0 for i in range(num_cols - len(array) % num_cols)])

    # Reshape the unicode message into a 2D array with cols number of columns
    #   and as many rows as necessary 
    return np.reshape(array, (-1, num_cols))


if len(sys.argv) < 2 or sys.argv[1] != 'encrypt' and sys.argv[1] != 'decrypt':
    print(sys.argv[1])
    raise ValueError('The second parameter has to be "encrypt" or "decrypt"')

elif sys.argv[1] == 'encrypt':
    # Read the message written in decrypted.txt
    decrypted_message = FileReader.read_message_file(FileReader.DECRYPTED_FILEPATH)

    # Convert each letter to its Unicode code point and add it to an array
    unicode_array = np.array([ord(character) for character in decrypted_message])

    key_matrix = FileReader.read_key_file()

    unicode_matrix = create_2d_matrix(unicode_array, len(key_matrix[0]))

    # Encrypt the matrix
    encrypted_matrix = np.matmul(unicode_matrix, key_matrix) % sys.maxunicode

    # Turn the encrypted numbers into Unicode and join it into a str
    encrypted_message = ''.join([chr(int(num)) for num in encrypted_matrix.flatten().tolist()])

    print(f'Original message: \n{decrypted_message}')
    print(f'\nKey matrix: \n{key_matrix}')
    print(f'\nEncrypted message: \n{encrypted_message}')

    # Write the encrypted message into encrypted
    with open(FileReader.ENCRYPTED_FILEPATH, 'w', encoding='utf-8') as encrypted_file:
        encrypted_file.write(encrypted_message)
  
elif sys.argv[1] == 'decrypt':
    encrypted_message = FileReader.read_message_file(FileReader.ENCRYPTED_FILEPATH)
    key_matrix = FileReader.read_key_file()

    # Turn the encrypted message into a matrix of ints
    encrypted_matrix = create_2d_matrix([ord(num) for num in encrypted_message], len(key_matrix[0]))

    # Obtain the modular inverse of the matrix's determinant
    determinant = int(np.linalg.det(key_matrix))
    modular_inverse = pow(determinant, -1, sys.maxunicode)

    # Multiply the encrypted_matrix by the inverse of the key to decrypt it
    decrypted_matrix = np.matmul(encrypted_matrix, np.matrix(key_matrix).getH()) * modular_inverse

    # Join the Unicode ints back into a str
    decrypted_message = ''.join([print(int(unicode)) for unicode in decrypted_matrix.flatten().tolist()])

    print(f'Encrypted message: \n{encrypted_message}')
    print(f'\nKey matrix: \n{key_matrix}')
    print(f'\nDecrypted message: \n{decrypted_message}')

    # write the decrypted message into decrypted.txt
    with open(FileReader.DECRYPTED_FILEPATHCRYPTED_FILEPATH, 'w', encoding='utf-8') as decrypted_file:
        decrypted_file.write(decrypted_message)