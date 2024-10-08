# very powerful, very easy to misuse 

def EVAL():
  x = 1
  expression = "x * 3 + x**2"
  result = eval(expression)
  assert result == 4

def EXEC():
  code = """
def greet(name):
  print(f"Hello, {name}!")

greet("Alice")
"""
  exec(code) # doesn't return anything

def COMPILE(): # if you're executing something many times you might want to pre-compile it
  code = 'print("Hello, World!")'
  compiledCode = compile(code, "<string>", "exec")
  exec(code)

def GLOBAL():
  global var
  var = 42
  globalVars = globals()
  assert globalVars["var"] == 42

  globalVars["var"] = 43
  assert globalVars["var"] == 43

def LOCAL():
  localVar = 10
  localVars = locals()
  assert localVars["var"] == 10
  # DONT MODIFY LOCALS

def VARS():
  class MyClass:
    def __init__(self):
      self.attribute = 543

  obj = MyClass()
  obj.attribute2 = "hello"

  varsDict = vars(obj)
  assert varsDict["attribute"] == 543
  assert varsDict["attribute2"] == "hello"

def IMPORT(): # really dangerous, DONT USE UNLESS REALLY NECESSERY
  math = __import__("math")
  assert math.sqrt(16) == 4

  math2 = __import__("math")
  assert math is math2

  import importlib # a much prefered and user friendly way to do imports
  math3 = importlib.import_module("math")
  assert math3 is math is math2
