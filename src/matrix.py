import numpy as np
from sys import maxunicode

class Matrix():
    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def multiply_matrices_mod(message_matrix: np.array, key_matrix: np.array) -> np.array:
        """
        Multiplies a matrix by a key matrix and mods it by the number of Unicode codepoints

        Parameters
        ----------
        message_matrix : np.array
            The message that is being encrypted or decrypted.
        key_matrix : np.array
            The key used to multiply the message.

        Returns
        -------
        np.array
            The product of message * key mod the number of Unicode codepoints
        """
        return np.matmul(message_matrix, key_matrix) % maxunicode