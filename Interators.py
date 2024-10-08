def iterNext(): # creates an iterator where each call on next returns the next item in the list
  iterator = iter([1, 2, 3])
  for x in [1, 2, 3]:
    assert next(iterator) == x

def enumerating(): # gets the index of each item as you iterate over them
  colors = ["red", "yellow", "green"]
  enumeratedColors = list(enumerate(colors))
  assert enumeratedColors[0] == (0, "red")
  assert enumeratedColors[1] == (1, "yellow")
  assert enumeratedColors[2] == (2, "green")

  for index, color in enumerate(colors): # usual way to use this
    print(index, color)

def zipping(): # allows to iterate over 2 lists at the same time
  numbers = [1, 2, 3]
  letters = ["a", "b", "c"]
  zipped = list(zip(numbers, letters))
  assert zipped[0] == (1, "a")
  assert zipped[1] == (2, "b")
  assert zipped[2] == (3, "c")

  for number, letter in zip(numbers, letters): # usual way to use this
    print(number, letter)
  
def reversing():
  numbers = [1, 2, 3]
  reversedNumbers = list(reversed(numbers))
  assert reversedNumbers == [3, 2, 1]
  assert next(iter(reversed({"a": 1, "b": 2, "c": 3}))) == "c"

def sorting():
  numbers = [5, 2, 8, 1, 3]
  sortedNumbers = sorted(numbers) # the result of sorted is always a list, no matter what you pass in
  assert sortedNumbers == [1, 2, 3, 5, 8]

def filtering(): # checks each element by a certain function (criteria)
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  evenNumbers1 = list(filter(lambda x: x % 2 == 0, numbers)) # for efficiency it doesn't make a copy, unless you tell it to do so
  assert evenNumbers1 == [2, 4, 6, 8, 10]
  evenNumbers2 = [x for x in evenNumbers if x % 2 == 0] # hand-made filter function
  assert evenNumbers1 == evenNumbers2

def mapping(): # applies a certain function to each element
  numbers = [1, 2, 3, 4, 5]
  squaredNumbers = list(map(lambda x: x**2, numbers)) # for efficiency it doesn't make a copy, unless you tell it to do so
  assert squaredNumbers == [1, 4, 9, 16, 25]
  squaredNumbers = [pow(x, 2) for x in numbers] # hand-made map function

def allAny():
  assert all([True, True, True])
  assert not all([True, False, True])

  assert any([True, True, True])
  assert any([False, False, True])

  assert all([]) # all of nothing is true
  assert not any([]) # any of nothing is false

def ranging():
  numbers = list(range(1, 6)) # the first argument is start (optional, default = 0), the second argument is stop
  assert numbers == [1, 2, 3, 4, 5]
  numbers2 = list(range(1, 6, 2)) # the third argument is the step (optional, default = 1)
  assert numbers2 == [1, 3, 5, 7, 9]

  for n in range(10, 2):
    assert n % 2 == 0
  
  assert 42 in range(100) # OK

def slicing():
  numbers = [1, 2, 3, 4, 5]
  assert numbers[slice(1, 4)] == [2, 3, 4] # first index is inclusive, second index is exclusive
  assert numbers[1:4] == [2, 3, 4] # same thing as above

  # x = 1:4 !ERROR! 
  x = slice(1, 4)

  assert numbers[slice(1, 4, 2)] == [2, 4] # the third argument is the step
  assert numbers[1:4:2] == [2, 4] 


