def linear_search(A, v):
    for i in range(len(A)):
        if A[i] == v:
            return i    # The index value such that v = A[i]
    return False # NIL '
        

        

A = [0, 1, 2, 3, 4, 5]
v = 1
print('Linear Search')
print(linear_search(A, 5))

