def OBJECT():
  sentinel = object()
  assert sentinel is not None

  d = {"val": None}
  val = d.get("val", sentinel) # the sentinel object doesn't mean anything, it is used as a default value, when values like 0 or None are usefull
  if (val is sentinel):
    print("not found")

def getAttr_setAttr_delAttr_hasAttr():
  class Example:
    def __init__(self):
      self.attribute = 100
  
  instance = Example()
  
  assert getattr(instance, 'attribute') == 100 # here the "attribute" can be used as a variable
  assert instance.attribute == 100

  assert getattr(instance, 'nonexistent', 'default') == 'default'

  instance.newAttribute = "value"
  setattr(instance, 'newAttribute', 'value')

  assert hasattr(instance, 'newAttribute')

  delattr(instance, 'attribute')
  del instance.attribute
  assert not hasattr(instance, 'attribute')

def DIR():
  numbers = [1, 2, 3]
  dirList = dir(numbers)
  assert "__len__" in dirList
  assert "__getitem__" in dirList
  # note: not guaranteed to be complete or correct 

def ID():
  obj = "Hello"
  objID = id("Hello")
  assert objID == id("Hello")

  s1 = {1, 2, 3}
  s2 = {1, 2, 3}
  assert s1 == s2
  assert not id(s1) == id(s2)

  assert s1 is s1 # this is the same as id(s1) == id(s1)
  assert s1 is not s2

def HASH(): # the hash number allows you to look up an object in a big hash table, without traversing the entire collection
  obj = "Hello"
  objHash = hash(obj)
  assert objHash == hash("Hello") 

def LEN():
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  length = len(numbers)
  assert length == 9

def ISINSTANCE():
  value = 100
  assert isinstance(value, int)
  assert not isinstance(value, str)

  assert isinstance(False, int) # FUN FACT: In python , booleans are integers

def ISSUBCLASS():
  class Parent:
    pass
  class Child(Parent):
    pass
  assert issubclass(Child, Parent)
  assert not issubclass(Parent, Child) # ! the order of the arguments matters

def Callable(): # checks if the thing you passed it is callable
  def func():
    return "Hello"
  
  class MyClass():
    def method(self):
      return "World"
  
  assert callable(func)
  assert callable(MyClass)
  obj = MyClass()
  assert callable(obj.method)
  assert not callable("Hello World")

def SUPER(): # goes one step back in inheritance hierarchy
  class Parent:
    def greet(self):
      return "Hello from Parent"
  class Child(Parent):
    def greet(self):
      return super().greet() + ", and hello from Child"

  child = Child()
  assert child.greet() == "Hello from Parent, and hello from Child"

def TYPE():
  number = 123
  typeOfNumber = type(number)
  assert typeOfNumber == int

def NEWTYPECREATION(): # create your own type
  def greet(self):
    return f"Hello {self.name}!"
  
  NewType = type("NewType", (object, ), {"name": "World", "greet": greet})
  instance = NewType()
  assert instance.name == "World"
  assert instance.greet() == "Hello World!"



