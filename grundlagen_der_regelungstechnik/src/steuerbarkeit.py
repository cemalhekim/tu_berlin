import numpy as np

def is_controllable(A, b):
    """
    Check if the system (A, b) is controllable.

    Parameters:
        A (ndarray): State matrix (n x n)
        b (ndarray): Input matrix (n x 1)

    Returns:
        bool: True if the system is controllable, False otherwise.
    """
    # Number of states (n)
    n = A.shape[0]

    # Construct the controllability matrix
    steuermatrix = b
    for i in range(1, n):
        steuermatrix = np.hstack((steuermatrix, np.linalg.matrix_power(A, i) @ b))

    # Check if the controllability matrix is full rank
    rank = np.linalg.matrix_rank(steuermatrix)
    
    return rank == n

# Example usage
A = np.array([[1, 1], [0, -1]])  # Example A matrix
b = np.array([[0], [1]])         # Example b vector

if is_controllable(A, b):
    print("The system is controllable.")
else:
    print("The system is NOT controllable.")