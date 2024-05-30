from errors import EmptyFileError
import numpy as np
from csv import reader

class FileReader():
  UNENCRYPTED_FILEPATH = '../input-output/unencrypted.txt'
  ENCRYPTED_FILEPATH = '../input-output/encrypted.txt'
  KEY_FILEPATH = '../input-output/key.csv'
  
  # takes in a filepath
  # reads the file and returns the content
  # if the file is empty, print out a warning
  @staticmethod
  def read_message_file(filepath):
    with open(filepath, 'r') as file:
      # read the message in the file
      message = file.read()
  
    try:
      # if the file is empty, raise an error
      if message == '':
        raise EmptyFileError
  
    # catcth the error 
    except EmptyFileError:
      # print out a warning saying that [file name] is empty
      print(f'The {filepath.split("/")[-1]} file is empty. Please enter a message into it.')
      exit(EmptyFileError)
    
    else:
      return message
  
  # reads the key.csv file and returns a matrix of the data
  # if the file is empty or does not contain an inversible matrix
  # prints out a corresponding warning
  @staticmethod
  def read_key_matrix():
    # matrix representing the key
    key_matrix = []
    
    try: 
      # read the key file
      with open(FileReader.KEY_FILEPATH, 'r') as key_file:
        # read the csv file
        read_csv = reader(key_file)
  
        # add each line as a row
        for line in read_csv:
          key_matrix.append([int(value) for value in line])
  
      # if the matrix is empty
      if key_matrix == []:
        # raise an error
        raise EmptyFileError
      
      # turn key_matrix into an array
      key_matrix = np.array(key_matrix)
  
      np.linalg.inv(key_matrix)
  
    # print a warning message if
    except EmptyFileError:
      print('The key.csv file is empty. Please fill it with a inversable matrix. Separate the elements with a comma(",").')
      exit(EmptyFileError)
  
    except ValueError:
      print('The matrix stored in key.csv is not inverseable. Please change it.')
      exit(ValueError)
  
    else:
      return key_matrix