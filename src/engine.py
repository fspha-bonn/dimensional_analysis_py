import numpy as np

def analyze(base, goal):
    """
    Arguments:
        base    List of base vectors in row form
        goal    Goal vector as list or array in row form

    Returns:
        error code
        list of powers

    Error Codes:
        0   Normal execution
        1   Base not linearily independent
    """
    #write base as matrix
    # transpose all base vectors into col-vectors
    base_vec = list()

    for row_vec in base:
        col_vec = np.transpose([row_vec])
        base_vec.append(col_vec)

    M = np.concatenate(base_vec, axis=1)

    #Test independence
    if np.linalg.det(M) == 0:
        return 1, None

    #invert Matrix
    M_rev = np.linalg.inv(M)

    # calculate powers
    return 0, np.dot(M_rev, goal)
