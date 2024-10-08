def strings():
  assert str(42) == "42"
  assert str(True) == "True"
  assert str(dict) == "<class 'dict'>"

def chrOrd(): # 2 inverse functions
  assert chr(65) == "A"
  assert ord("A") == 65
  assert chr(ord(100)) == 100

def binOctHex(): # representations of numbers in binary, octary and hexary systems
  assert bin(42) == "0b101010"
  assert oct(42) == "0o52"
  assert hex(42) == "0x2a"

  assert int("0b101010", 2) == 42
  assert int("0o52", 8) == 42 # int can reverse this process by passing the base that was used as the second argument
  assert int("0x2a", 16) == 42

def formating():
  name = "Alice"
  age = 31

  formatedString = f"Name: {name}, Age: {age}"
  formatedString = "Name: {}, Age: {}".format(name, age)
  assert formatedString == "Name: Alice, Age: 31"

  formatedString = f"Name: {name}, Age: {age:x}" #turn into hexary system
  assert formatedString == "Name: Alice, Age: 1f"

  formatedString = f"Name: {name}, Age: {age:b}" #turn into binary system
  assert formatedString == "Name: Alice, Age: 11111"

  formatedString = f"Name: {name}, Age: {age:o}" #turn into octary system
  assert formatedString == "Name: Alice, Age: 1f"

  #how to change it
  class MyCls:
    def __format__(self, formatSpecs = None):
      if (formatSpecs == "x"):
        return "<HEX>"
      if (formatSpecs == "o"):
        return "<OCT>"
      if (formatSpecs == "b"):
        return "<BIN>"
      if (formatSpecs == "specialBase"):
        return "<SPECIAL>"
      return "<NORMAL>"

def inputPrint(): # pauses your program until user enters at terminal
  name = input("Enter your name: ")
  assert isinstance(name, str)
  print(name)
  print(name, file=sys.stderr) # the file parameter specifies where the messeage should be written
  

