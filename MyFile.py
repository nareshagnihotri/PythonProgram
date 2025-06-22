"""
Modes:
'r' (read): Opens for reading (default). Raises an error if the file doesn't exist.
'w' (write): Opens for writing. Creates the file if it doesn't exist, or truncates (empties) it if it does.
'a' (append): Opens for writing, appending data to the end of the file. Creates the file if it doesn't exist.
'x' (exclusive creation): Creates a new file. Raises an error if the file already exists.
'b' (binary): Opens in binary mode (e.g., for images, executables).
't' (text): Opens in text mode (default).
'+' (read and write): Combines with other modes (e.g., 'r+', 'w+', 'a+').
"""


# z = input("Enter text to append to the file DA1: ")
# x = open("DA1.csv", "a")
# x.write(z + "\n")
# x.close()




# y = open("DA1.csv", "r")
# line = y.readline()
# for line in y:
#     print(line.strip())
# y.close()


z = input("Enter text to append to the file DA1: ")
x = open("DA1.csv", "a+")
x.write(z + "\n")
x.close()

y = open("DA1.csv", "r+")
line = y.readline()
for line in y:
    print(line.strip())
y.close()
