def APPEND():
  people: list[str] = ["Obama", "Trump", "Elon"] #this is type assertion for lists (you can have 1 or more type in square brackets [])

  # list.append(False) !ERROR!

  people.append("Elon") # adds the item to the end of the list
  assert people == ['Obama', 'Trump', 'Elon']

def CLEAR():
  values: list[bool] = [True, True, False, True]
  values.clear() # removes everything from the list
  assert values == []

def COPY():
  numbers: list[int] = [1, 2, 3, 4, 5]
  copyNumbers: list[int] = numbers.copy() # creates a shallow copy of the list, which means we can edit it, without any side-effects 
  copyNumbers.append(6)
  assert numbers == [1, 2, 3, 4, 5]
  assert copyNumbers == [1, 2, 3, 4, 5, 6]

  # !!ONLY WORKS FOR 1D LISTS!! 
  employees: list[str] = ["Bob", ["John", "Mark"], "George"]
  copyEmployees: list[str] = employees.copy()
  copyEmployees.remove("George")
  copyEmployees[1][1] = "Mac" #both the original and the copy got changed
  assert employees == ['Bob', ['John', 'Mac'], 'George']
  assert copyEmployees == ['Bob', ['John', 'Mac']] 
  # DO NOT COPY MULTI-DIMENSIONAL LISTS!!

def COUNT():
  people: list[str] = ["Mac", "Alice", "John", "Alice", "John", "John"]
  assert people.count("Mac") == 1
  assert people.count("Alice") == 2
  assert people.count("John") == 3
  assert people.count("Bob") == 0

def EXTEND():
  list1: list[str] = ["Europe", "Asia", "Australia"]
  list2: list[bool] = [True, False, False, False]
  list1.extend(list2) # the extended lists don't have to be the same type 
  assert list1 == ["Europe", "Asia", "Australia", True, False, False, False] 
  list1.extend([1]) # an integer isn't iterable so you have to put brackets around it
  assert list1 == ["Europe", "Asia", "Australia", True, False, False, False, 1]

def INDEX():
  fruits: list[str] = ["Apple", "Banana", "Strawberry"]
  assert fruits.index("Banana") == 1 
  # assert fruits.index("Orange") == -1 !ERROR!

def INSERT():
  people: list[str] = ["Mario", "Elon", "Trump"]
  people.insert(1, "Luigi") # the index of insertion + the value being inserted
  assert people == ["Mario", "Luigi", "Elon", "Trump"]
  
  people.insert(10000, "Obama") # if the index is bigger than the list, it will act as if you appended it to the end
  assert people == ["Mario", "Luigi", "Elon", "Trump", "Obama"]

  people.insert(-10000, "Lincoln") # if the index is smaller than 0, it will add it to the start
  assert people == ["Lincoln", "Mario", "Luigi", "Elon", "Trump", "Obama"]

def POP():
  nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
  assert nums.pop() == 8 # without parameters, it removes the last element and returns it
  assert nums == [1, 2, 3, 4, 5, 6, 7]

  assert nums.pop(0) == 1 # with parameters it removes the person at that index
  assert nums == [2, 3, 4, 5, 6, 7]

def REMOVE():
  nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
  nums.remove(5)
  assert nums == [1, 2, 3, 4, 6, 7, 8]
  # nums.remove(9) !ERROR!
  
def REVERSE():
  nums: list[int] = [1, 2, 3, 4, 5]
  assert nums.reverse() == [5, 4, 3, 2, 1]

def SORT():
  people: list[str] = ["Bob", "John", "Alice", "Trump", "alice"] 

  people.sort() # sorts by ASCII key, alphabetically, except lower case letters go later
  assert people == ["Alice", "Bob", "John", "Trump", "alice"]

  people.sort(key = lambda x: x.lower()) # an optional parameter to sort however you want
  assert people == ["Alice", "alice", "Bob", "John", "Trump"]

  people.sort(key = lambda x: x.lower(), reverse = True) # you can reverse any sort function
  assert people == ["Trump", "John", "Bob", "Alice", "alice"]

  people.sort(key = lambda x: len(x), reverse = False)
  assert people == ['Bob', 'John', 'Trump', 'Alice', 'alice'] # another example

def IN(): # worse than sets for this O(n) complexity
  assert 2 in [1, 2, 3] 
  assert not 4 in [1, 2, 3]
