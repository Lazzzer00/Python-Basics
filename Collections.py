# these are type-assertion collection types

def dictionaries():
  person = {"name": "Lazzzer", "age": 15, "city": "New York"}
  person = dict(name="Lazzzer", age=15, city="New York") # these are the ways to difine the same dictionary
  person = dict([("name", "Lazzzer"), ("age", 15), ("city", "New York")])

  assert person["name"] == "Lazzzer"
  assert person["age"] == 15
  assert person["city"] == "New York"

def lists(): # lists and arrays are the same, but lists can be heterogeneous, while arrays are homogeneous
  fruitSet = {"banana", "apple", "orange"};
  fruits = list(fruitSet);
  assert fruits[0] in fruitSet
  assert len(fruits) == 3;

def tuples(): # the same as a list, but cannot be changed
  coordinates = tuple([3, 4])
  coordinates = (3, 4)
  assert coordinates[0] == 3
  assert coordinates[1] == 4
  # coordinates[0] = 5 !ERROR!

def sets(): # sets cannot contain duplicates
  fruitList = ["apple", "cherry", "apple", "banana"]
  fruits = set(fruitList)
  fruits = {"apple", "cherry", "banana"}
  assert len(fruits) == 3
  assert "banana" in fruits

def frozensets(): # the same as a set, but cannot be changed
  colorList = ["red", "blue", "green", "green"]
  colors = frozenset(colorList)
  assert len(colors) == 3
  assert "red" and "blue" in colors
  # colors.add("yellow") !ERROR!

