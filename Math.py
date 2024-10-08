#the next 4 functions are type-conversion functions

#an empty string converts to false, a non-empty string converts to true. Zero converts to false and any other number converts to true.
def boolType():
  isNotEmpty = bool("Hello")
  isEmpty = bool("")
  isZero = bool(0)
  isNotZero = bool(10)

  assert isNotEmpty is True
  assert isEmpty is False
  assert isZero is False
  assert isNotZero is True

def intType():
  stringNum = "123"
  intNum = int(stringNum)
  assert intNum == 123

def floatType():
  stringNum = "123.45"
  floatNum = float(stringNum)
  assert floatNum == 123.45

#the imaginaty unit "i" is assesed as "j" in python
def complexType():
  realPart = 4.5
  imaginaryPart = 6.2
  complexNum = complex(realPart, imaginaryPart)
  assert complexNum == 4.5 + 6.2j

#math functions

def maxMin():
  numbers = [4, 5, 6, 7, 2, 3, 4, 5, 6, 7];
  assert max(numbers) == 7
  assert min(numbers) == 2

  assert max(5, 4, 8, 1) == 8
  assert min(5, 4, 8, 1) == 1

def dividerModule():
  #quotient, remainder = 10 // 3, 10 % 3
  quotient, remainder = divmod(10, 3)
  assert (quotient, remainder) == (3, 1)

def absoluteValue():
  assert abs(-10) == 10
  assert abs(10.0) == 10.0
  assert abs(3 + 4j) == 5 # for complex numbers it return the distance from the origin on the complex plane

def power():
  assert 2**3 == 8
  assert pow(2, 3) == 8
  assert pow(2, 3, 5) == 3 # (2^3) % 5, the third argument is optional

def rounding():
  assert round(3.14159, 2) == 3.14
  assert round(2.675, 2) == 2.67 # Warning! float errors
  assert round(42069, -3) == 42000 # Used to clear off digits to 0 from the right

def summing():
  numbers = [1, 2, 3, 4, 5, 6]
  assert sum(numbers) == 21
  evenCount = sum(1 for x in numbers if x % 2 == 0)
  assert evenCount == 3




