print("\n -------------------")

text = "Привет, мир!"
print(text[8:11])   # мир
print(text[:6])     # Привет
print(text[8:])     # мир!     
print(text[:])      # Привет, мир!      
print(text[::2])    # Пие,мр       

print("\n -------------------")

text = "Pushkin"
for i, letter in enumerate(text):
    print(f"{i}. {letter}")

print("\n -------------------")

# "hello, World!".capitalize()  => Hello, world!
# "Hello, world!".count("l")    => 3
# "Hello, world!".find("o")     => 4, otherways -1
# "Hello, world!".index("o")    => 4, otherways ValueError
# "stringBCCA".rstrip("ABC")    => "string"
# "one, two, three".split(", ") => ["one", "two", "three"]

# "hello, world!".title()   => "Hello, World!"
# "Hello, world!".upper()   => "HELLO, WORLD!"
# "123".zfill(5)            => "00123"
# "abc123".isalnum()        => True
# "Letters".isalpha()       => True
# "123".isdigit()           => True
# "word123".islower()       => true
# "WORD123".isupper()       => True
# "text".ljust(10, "=")     => "text======"

# " Hello, world! ".replace(" ", "")    => "Hello,world!"
# "Hello, world!".startswith("Hello")   => True
# "abc Hello, world! cba".strip(" abc") => "Hello, world!"
# "Hello, world!".endswith("world!")    => True

# a = ["1", "2", "3"] 
# "; ".join(a)              => "1; 2; 3"
