# these aren't really methods, but they rather say to the machine what the next part of the code will do
def example_classmethod_property_staticmethod():
  class MyClass:
    def __init__(self, value):
      self._value = value

    @property
    def value(self):
      return self._value
    
    @value.setter
    def value(self, val):
      self._value = val
    
    @classmethod
    def class_method(cls):
      return cls.__name__

    @staticmethod
    def static_method():
      return "Static method called"
    
  instance = MyClass(100)

  assert instance.value == 42
  instance.value = 0

  assert instance.class_method() == "MyClass"
  assert MyClass.static_method() == "Static method called"
