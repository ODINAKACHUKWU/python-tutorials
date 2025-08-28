"""Module demonstrating different data types."""

# 1. Text type:
NAME = "John Doe"  # str: String type

# 2. Number types:
AGE = 30  # int: Integer type
HEIGHT = 5.9  # float: Floating point type
COMPLEX_NUM = 2j  # complex: Complex type

# 3. Sequence types:
FRUITS = ["apple", "banana", "cherry"]  # list: List type
COLORS = ("red", "green", "blue")  # tuple: Tuple type
RANGE = range(1, 10)  # range: Range type

# 4. Mapping type:
PHONEBOOK = {"John": 1234567890, "Jane": 9876543210}  # dict: Dictionary type

# 5. Set types:
UNIQUE_FRUITS = {"apple", "banana", "cherry"}  # set: Set type
# frozenset: Immutable Set type
UNMODIFIABLE_FRUITS = frozenset({"apple", "banana", "cherry"})

# 6. Boolean type:
IS_ACTIVE = True  # bool: Boolean type

# 7. Binary types:
BINARY_DATA = b"Hello, World!"  # bytes: Bytes type
# memoryview: Memory view type
MEMORY_VIEW = memoryview(bytes(5))
BYTE_ARRAY = bytearray(b"Hello, World!")  # bytearray: Mutable Bytes type

# 8. None type:
NOTHING = None  # NoneType: None type

print(NAME)
print(AGE)
print(HEIGHT)
print(COMPLEX_NUM)
print(FRUITS)
print(COLORS)
print(RANGE)
print(PHONEBOOK)
print(UNIQUE_FRUITS)
print(UNMODIFIABLE_FRUITS)
print(IS_ACTIVE)
print(BINARY_DATA)
print(MEMORY_VIEW)
print(BYTE_ARRAY)
print(NOTHING)
