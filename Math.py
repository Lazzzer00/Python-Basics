#an empty string converts to false, a non-empty string converts to true. Zero converts to false and any other number converts to true.
def BOOL():
  isNotEmpty = bool("Hello")
  isEmpty = bool("")
  isZero = bool(0)
  isNotZero = bool(10)

  assert isNotEmpty is True
  assert isEmpty is False
  assert isZero is False
  assert isNotZero is True

def INT():
  stringNum = "123"
  intNum = int(stringNum)
  assert intNum == 123

def FLOAT():
  stringNum = "123.45"
  floatNum = float(stringNum)
  assert floatNum == 123.45

#the imaginaty unit "i" is assesed as "j" in python
def COMPLEX():
  realPart = 4.5
  imaginaryPart = 6.2
  complexNum = complex(realPart, imaginaryPart)
  assert complexNum == 4.5 + 6.2j

#math functions

def MAX_MIN():
  numbers = [4, 5, 6, 7, 2, 3, 4, 5, 6, 7];
  assert max(numbers) == 7
  assert min(numbers) == 2

  assert max(5, 4, 8, 1) == 8
  assert min(5, 4, 8, 1) == 1

def DIVMOD():
  #quotient, remainder = 10 // 3, 10 % 3
  quotient, remainder = divmod(10, 3)
  assert (quotient, remainder) == (3, 1)

def ABS():
  assert abs(-10) == 10
  assert abs(10.0) == 10.0
  assert abs(3 + 4j) == 5 # for complex numbers it return the distance from the origin on the complex plane
  # 3^2 + 4^2 = 5^2 
def POW():
  assert 2**3 == 8
  assert pow(2, 3) == 8
  assert pow(2, 3, 5) == 3 # (2^3) % 5, the third argument is optional

def ROUND():
  assert round(3.14159, 2) == 3.14
  assert round(2.675, 2) == 2.67 # Warning! float errors
  assert round(42069, -3) == 42000 # Used to clear off digits to 0 from the right

def SUM():
  numbers = [1, 2, 3, 4, 5, 6]
  assert sum(numbers) == 21
  evenCount = sum(1 for x in numbers if x % 2 == 0)
  assert evenCount == 3






