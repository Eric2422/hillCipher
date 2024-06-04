import numpy as np

class FileReader():
    INPUT_OUTPUT_DIR = '../input_output'
    DECRYPTED_FILEPATH = f'{INPUT_OUTPUT_DIR}/decrypted.txt'
    ENCRYPTED_FILEPATH = f'{INPUT_OUTPUT_DIR}/encrypted.txt'
    KEY_FILEPATH = f'{INPUT_OUTPUT_DIR}/key.csv'
    
    @classmethod
    def read_message_file(cls, filepath: str):
        """
        Reads a file and return the string in it.

        Parameters
        ----------
        filepath : str
            The path to the file to be read

        Returns
        -------
        str
            The data in the file

        Raises
        ------
        ValueError
            If the file is empty or non-existent
        """
        with open(filepath, 'r') as file:
            message = file.read()
    
        try:
            # if the file is empty, raise an error
            if message == '':
                raise ValueError
    
        except ValueError:
            # print out a warning saying that [file name] is empty
            print(f'The {filepath.split("/")[-1]} file is empty. Please enter a message into it.')
            exit(ValueError)
      
        else:
            return message
    
    @classmethod
    def read_key_file(cls):
        """
        Read the key.csv file and returns a 2D array of the key.

        Returns
        -------
        np.array
            The key as a 2D array

        Raises
        ------
        ValueError
            When the file is empty or the matrix is not invertible
        """
        key_matrix = np.genfromtxt(cls.KEY_FILEPATH, delimiter=',')

        try:
            np.linalg.inv(key_matrix)
            return key_matrix
        
        except ValueError:
            print("Enter an invertible matrix into key.csv")
            exit(ValueError)