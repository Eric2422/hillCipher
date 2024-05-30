import numpy as np
from file_reader import FileReader

# takes a !D array and a number of columns
# returns a 2D array with 0s to pad the end
def create_2d_matrix(array, num_cols):
  # reshape raises an exception if number of elements
  # does not match the array dimensions

  # if the message does not fit into the array
  if len(array) % num_cols != 0:
    # pad it with as many 0s as necessary
    array = np.append(array, [0 for i in range(num_cols - len(array) % num_cols)])
    
  # reshape the unicode message into a 2D array with cols number of columns
  # -1 indicates that the array will have as many rows as necessary
  return np.reshape(array, (-1, num_cols))

option = None
while not(option == 'e' or option == 'd'):
  option = input('Encrypt(e) or decrypt(d) (case-insensitive): ')

# if the user wants to encrypt
if option == 'e':
  # read the message written in unencrypted.txt
  unencrypted_message = FileReader.read_message_file(FileReader.UNENCRYPTED_FILEPATH)
  
  # convert each letter to its Unicode code point and add it to an array
  unicode_array = np.array([ord(character) for character in unencrypted_message])

  key_matrix = FileReader.read_key_matrix()

  unicode_matrix = create_2d_matrix(unicode_array, len(key_matrix[0]))
  
  # the message encrypted and in matrix form
  encrypted_matrix = np.matmul(unicode_matrix, key_matrix)

  # turn the matrix into a list of strings and then join the list into a string separated by "-"
  encrypted_message = '-'.join([str(num) for num in encrypted_matrix.flatten().tolist()])
  
  print(f'Original message: \n{unencrypted_message}')

  print(f'\nKey matrix: \n{key_matrix}')

  print(f'\nEncrypted message: \n{encrypted_message}')
    
  # write the encrypted message into encrypted
  with open(FileReader.ENCRYPTED_FILEPATH, 'w') as encrypted_file:
    encrypted_file.write(encrypted_message)
  
# if the user wants to decrypt
else:
  # read the encrypted file
  encrypted_message = FileReader.read_message_file(FileReader.ENCRYPTED_FILEPATH)
  
  # read the key_matrix
  key_matrix = FileReader.read_key_matrix()
  
  # turn the encrypted message into a matrix of ints
  encrypted_matrix = create_2d_matrix([int(num) for num in encrypted_message.split('-')], len(key_matrix[0]))
  
  # multiply the encrypted_matrix by the inverse of the key to dencrypt it
  decrypted_matrix = np.matmul(encrypted_matrix, np.linalg.inv(key_matrix))

  # convert the matrix into an decrypted message
  decrypted_message = ''.join([chr(round(unicode)) for unicode in decrypted_matrix.flatten().tolist()])

  print(f'Encrypted message: \n{encrypted_message}')

  print(f'\nKey matrix: \n{key_matrix}')

  print(f'\nDecrypted message: \n{decrypted_message}')
  
  # write the decrypted message into unencrypted.txt
  with open(FileReader.UNENCRYPTED_FILEPATH, 'w') as unencrypted_file:
    unencrypted_file.write(decrypted_message)