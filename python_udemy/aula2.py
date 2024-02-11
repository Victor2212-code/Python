# \r \n -> CRLF
# \n - LF

print(12, 34, 1011, sep='-', end="##\r \n")
print(56, 78, sep='_', end='\n')
print(9, 10, sep='-', end='\n')