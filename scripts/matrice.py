def matrice():
    M = [[1, 0, 1, 0], [1, 1, 1, 0]]
    B = [[1, 1, 0, 0], [1, 0, 0, 1]]
    if len(M) != len(B) or len(M[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition")

    result = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]

    # Perform matrix addition
    for i in range(len(M)):
        for j in range(len(M[0])):
            result[i][j] = M[i][j] + B[i][j]

    return result

def binary_matrice():
    A = 0b1110100101101001
    C = 0b1001010010010101
    R = 0b0

    """
                11 10 10 01 
                01 10 10 01
    10 01 01 00 
    10 01 01 01

    We need to extract bits 2 by 2 so we can add them
    """
    n_size = 2  #number of lignes
    k_size = 4  #number of columns
    b_size = 2  #number of bits per elements

    A_bit_size = A.bit_length()
    C_bit_size = C.bit_length()

    while (A>0):

        A>>=b_size


nombre = 0b10101100
bits_deplaces = (nombre & ((1 >> 2) - 1))  # 'n' est le nombre de bits décalés

nombre_deplace = nombre >> 3  # Exemple de décalage de 2 bits vers la gauche

print("Nombre original:", bin(nombre))
print("Nombre déplacé:", bin(nombre_deplace))
print("Bits déplacés:", bin(bits_deplaces))



print (binary_matrice())