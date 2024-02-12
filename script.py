# Opérateurs:
# ET logique
a = 0b1010 & 0b0101

# OU logique
a = 0b1010 | 0b0101

# OU exclusif (xor)
a = 0b1010 ^ 0b0101

# shift
a = 0b1010 >> 1
b = 0b0101 << 1



# Modifications:
#Définition du 3e bit à 1
n = 0b1010 | (1 << 2);  

#Effacement du 5e bit (le met à 0)
n = 0b11011 & ~(1 << 4);  

#Inversion du 2e bit
n = 0b1111 ^ (1 << 1);



# Algorithmes:

# Concaténation de deux nombres binaires
# 1010 + 1111 = 10101111 avec 4 la taille en bit de 1010
0b1010 | (0b1111 << 4)