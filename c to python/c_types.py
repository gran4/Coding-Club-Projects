import ctypes

# Load the shared library
lib = ctypes.CDLL('./c to python/libexample.so')  # or './example.dll' on Windows

# Call the 'add' function
result = lib.add(5, 3)
print(f"5 + 3 = {result}")

# Call the 'hello' function
lib.hello()

# gcc -shared -o libexample.so -fPIC example.c
