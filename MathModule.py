import math
# all returns are floats, unless specified otherwise

def CEIL(): # returns the smallest integer greater than or equal to the given value
  assert math.ceil(4.5) == 5
  assert math.ceil(2) == 2 # for integer values, it returns an integer  

def FLOOR(): # returns the greatest integer less than or equal to the given value
  assert math.floor(3) == 3 # for integer values, it returns an integer
  assert math.floor(5.42) == 5 

def TRUNC(): # Return x with the fractional part removed, leaving the integer part. 
  # This rounds toward 0: trunc() is equivalent to floor() for positive x, and equivalent to ceil() for negative x.
  assert math.trunc(5.23) == 5
  assert math.trunc(-5.74) == -5

def COPYSIGN(): # returns a float with the magnitude (absolute value) of x, but the sign of y
  x = 1.0
  y = -0.0
  assert math.copysign(x, y) == -1.0 
  assert math.copysign(y, x) == 0.0

def COMB(): # return the number of ways to choose k items from n items without repetition and without order
  # evaluates to n! / (k! * (n - k)!) when k <= n and evaluates to zero when k > n.
  assert math.comb(3, 2) == 3
  assert math.comb(3, 3) == 1
  assert math.comb(3, 4) == 0 

def FACTORIAL(): # return n factorial as an integer. raises ValueError if n is not integral or is negative.
  assert math.factorial(1) == 1
  assert math.factorial(2) == 2
  assert math.factorial(5) == 120
  # assert math.factorial(5.1) !ERROR!
  # assert math.factorial(-1) !ERROR!

def GCD(): # return the greatest common divisor of the specified integer arguments.
  assert math.gcd(1, 2) == 1
  assert math.gcd(0, 0, 0) == 0
  assert math.gcd() == 0

def ISFINITE(): # return True if x is neither an infinity nor a NaN, and False otherwise. (Note that 0.0 is considered finite.)
  assert not math.isfinite(math.nan) 
  assert not math.isfinite(float("inf"))
  assert math.isfinite(0)
  assert math.isfinite(10)

def IFINF(): # return True if x is a positive or negative infinity, and False otherwise.
  assert math.isinf(float("inf"))
  assert math.isinf(float("-inf"))
  assert not math.isinf(1) 

def ISNAN(): # return True if x is a NaN (not a number), and False otherwise.
  assert math.isnan(math.nan)
  assert not math.isnan(10)

def PERM(): # return the number of ways to choose k items from n items without repetition and with order.
  # Evaluates to n! / (n - k)! when k <= n and evaluates to zero when k > n. k is optional, and defaults to None
  assert math.perm(5) == math.factorial(5)
  assert math.perm(5, 3) == 60 # 5! / (5 - 3)! = 120 / 2 = 60

def PROD(): # Calculate the product of all the elements in the input iterable. The default start value for the product is 1.
  nums = [2, 3, 4, 5, 6]
  assert math.prod(nums) == 720
  assert math.prod(nums, start=0.5) == 360
 
def REMAINDER(): # return the remainder of x // y. For finite x and finite nonzero y, this is the difference x - n*y, where n is the closest integer to the exact value of the quotient x / y.
  assert math.remainder(7, 3) == 1
  assert math.remainder(10, 2) == 0

# LOGARITHMIC AND EXPONENTIAL FUNCTIONS 
def EXP(): # return e to the power of x
  x = 2.465
  result = math.exp(x) # most precision
  result = math.e ** x
  result = pow(math.e, x)

def LOG(): # With one argument, return the natural logarithm of x (to base e).
  # With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).
  assert math.log(math.e) == 1
  assert math.log(100, 10) == 2

def LOG10(): # Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).
  assert math.log10(1) == 0
  assert math.log10(100) == 2
  assert math.log10(1000000) == 6

def LOG2(): # Return the base-2 logarithm of x. This is usually more accurate than log(x, 2).
  assert math.log2(1) == 0
  assert math.log2(8) == 3
  assert math.log2(64) == 6

# TRIGONOMETRY FUNCTIONS
def SIN(): # Return the sine of x radians.
  assert math.sin(2*math.pi) == 0
  assert math.sin(math.pi / 2) == 1

def ASIN(): # Return the arc sine of x, in radians. The result is between -pi/2 and pi/2.
  assert math.asin(0) == 0
  assert math.asin(1) == math.pi / 2

def COS(): # Return the cosine of x radians.
  assert math.sin(2*math.pi) == 1
  assert math.sin(math.pi / 2) == 0

def ACOS(): # Return the arc cos of x, in radians. The result is between -pi/2 and pi/2.
  assert math.acos(0) == math.pi / 2
  assert math.asin(1) == 0

def TAN(): # Return the tangent of x radians.
  assert math.tan(0) == 0
  assert math.tan(math.pi / 4) == 1

def ATAN(): # Return the arc tangent of x, in radians. The result is between -pi/2 and pi/2.
  assert math.atan(0) == 0
  assert math.atan(1) == math.pi / 4

# ANGLE CONVERSIONS 
def DEGREES(): # Convert angle x from radians to degrees.
  assert math.degrees(math.pi) == 180
  assert math.degrees(0) == 0

def RADIANS(): # Convert angle x from degrees to radians.
  assert math.radians(180) == math.pi
  assert math.radians(0) == 0

# CONSTANTS 
PI = math.pi # The mathematical constant π = 3.141592…, to available precision.
E = math.e # The mathematical constant e = 2.718281…, to available precision.
TAU = math.tau # The mathematical constant τ = 6.283185…, to available precision. Tau is a circle constant equal to 2π.
INF = math.inf # A floating-point positive infinity. (For negative infinity, use -math.inf.) Equivalent to the output of float('inf'). 
NAN = math.nan # A floating-point “not a number” (NaN) value. Equivalent to the output of float('nan').