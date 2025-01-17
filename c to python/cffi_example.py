from cffi import FFI
ffi = FFI()

# Define the C function signatures
ffi.cdef("""
    int add(int a, int b);
    void hello();
""")

# Load the shared library
lib = ffi.dlopen("./libexample.so")

# Call the C functions
result = lib.add(5, 3)
print(f"5 + 3 = {result}")

lib.hello()

# python & c
# c vs c++
# algorithm problems
# how to use chatgpt correctly
