import numpy as np

def invertible(vectors):
    # Generate matrix by padding column vectors together
    matrix = np.concatenate([vectors], axis = 1).transpose()
    dims = matrix.shape

    if not dims[0] == dims[1]:
        raise ValueError("Inappropriate amount of vectors supplied,\nor vectors of wrong shape. Matrix not invertible")
        return

    return not (np.linalg.det(matrix) == 0)

def __iterate_unique_indices__(vec, max):
    """
    Takes vector of indices and iterates to the next unique index-combination.
    """
    i = -1
    while i >= -len(vec):
        vec[i] += 1
        if not vec[i] > max:
            break

        vec[i] = 0
        i -= 1

    if len(vec) == len(np.unique(vec)):
        return vec
    else:
        return __iterate_unique_indices__(vec, max)


def complete_base(vectors, dim = 7):
    """
    Takes vectors and returns completed base as list of vectors.
    """

    n = len(vectors)

    # pick vector from producing system
    # and check whether the resulting system is
    # linerarly independent. Repeat dim-n times
    E = np.zeros((dim,dim))
    for i in range(dim):
        E[i][i] = 1

    #pick dim-n vectors
    n = dim-len(vectors)
    indices = np.zeros(n)
    for i in range(n):
        indices[i] = i

    is_invertible = False
    count = 0
    maxcount = (dim-1)**n

    while not is_invertible:
        if count > maxcount:
            raise ValueError("Could not construct a base. Provided Vectors may dependent.")
            return

        count += 1
        vec = list(vectors.copy())
        for i in range(n):
            vec.append(E[:,int(indices[i])])

        is_invertible = invertible(vec)
        if not is_invertible:
            indices = __iterate_unique_indices__(indices, dim-1)


    return np.concatenate([vec], axis = 1).transpose()


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
