

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]
# alphabet.shift(1)
print("hello")

direction = input("Type 'encode' to encrypt, type 'decode to decrypt\n")
plain_text = input("Type your message: \n").lower()
shift_amount = int(input("Type the shift number: \n"))


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#       position = alphabet.index(letter)
#       new_position = position + shift_amount
#       new_letter = alphabet[new_position]
#       cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")



# def decrypt(encrypted_text, shift_amount):
#     decipher_text = ""
#     for letter in encrypted_text:
#       position = alphabet.index(letter)
#       new_position = position - shift_amount
#       decipher_text += alphabet[new_position]
#     print(f"The decoded text is {decipher_text}")


# if direction == 'encode'.lower():
#    encrypt(plain_text, shift_amount)  



# if direction == 'decode'.lower():
#    decrypt(encrypted_text=plain_text, shift_amount = shift_amount)


def ceaser(direction, plain_text, shift_amount):
      cipher_text = ""
      decipher_text = ""
      if direction == 'encode'.lower():
        for letter in plain_text:
          position = alphabet.index(letter)
          new_position = position + shift_amount
          new_letter = alphabet[new_position]
          cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")
      if direction == 'decode'.lower():
        for letter in plain_text:
          position = alphabet.index(letter)
          new_position = position - shift_amount
          decipher_text += alphabet[new_position]
        print(f"The decoded text is {decipher_text}")  


ceaser(direction=direction, plain_text=plain_text, shift_amount=shift_amount)



# def greet():
#   print("heloo")
#   print("world")
#   print("from Justin")


# greet()

# def greet_with_name(person):
#   print(f"Im going to the store with {person}")

# name = "Justin"

# greet_with_name(name)
# greet_with_name(8)


# def greet_with_name_location( names, local = "los andgles"):
#   print(f"My name is {names}")
#   print(f"My location is {local}")

# greet_with_name_location("Mickal", "New Orleans")

# greet_with_name_location(local="london",names= "Billy")



# def paint_calc(height, width, cover):
#   num_cans = (height/width)/ cover 
#   round_up_cans = math.ceil(num_cans)
#   print(round_up_cans)

# test_h = int(input("please enter height\n"))
# test_w = int(input("Please enter width\n"))
# coverage = 5

# paint_calc(test_h, test_w, coverage)


# def prime_checker(number):
#   is_prime = False
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = True
#   if is_prime:
#       print("this is a prime number")
#   else:
#       print("not a prime number")


# prime_checker(4)

# def primes_checker(numbers):
#    is_prime = False
#    for i in range(2, numbers):
#       if numbers % i == 0:
#          is_prime = True
#    if is_prime:
#       print("this is a prime num")