def SET():
  s1 = set([x for x in range(5)]) # s1 = {1,2,3,4,5}
  s2 = set() # s2 = {} (empty set)

def ADD():
  s1 = set([x for x in range(5)]) # s1 = {1,2,3,4,5}
  s1.add(6) # s1 = {1,2,3,4,5,6}

def UPDATE():
  s1 = set([x for x in range(5)])
  s1.update([6, 7, 8]) # add for multiple values
  s2 = set([9, 10]) 
  s1.update(s2) # 
  # equivalent to s1.update([6,7,8], s2)

def REMOVE_DISCARD():
  s1 = set([x for x in range(5)])
  s1.remove(5) # s1 = {1,2,3,4}
  # s1.remove(9) !KeyERROR!
  s1.discard(9) # s1 = {1,2,3,4} 
  # (doesn't throw an error if the element doesn't exist)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

def INTERSECTION():
  s4 = s1.intersection(s2) # s4 = {2, 3}
  s4 = s1.intersection(s2, s3) # s4 = {3}

def DIFFERENCE():
  s4 = s1.difference(s2) # s4 = {1}
  s4 = s2.difference(s1, s3) # s4 = {}

def SYMMETRIC_DIFFERENCE():
  s4 = s1.symmetric_difference(s2) # s4 = {1, 4}
  # takes the difference of s1 with s2 + difference of s2 with s1

def IN():
  assert s2.difference(s1) in s3 
  # better performance O(1) than lists O(n) with the in operator 

