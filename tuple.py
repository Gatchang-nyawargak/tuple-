k= (2,45,6,8,10)
print(k)
# operations of acessing tuples
# by index
print(k[2])
# slicing
print(k[1:])
print(k[:4])
# checking for membership
if 10 in k:
    print("found")
else:
    print("not found")
# Repetition
print(k*3)
# finding max
print(max(k))
# finding minimum
print(min(k))
y=("Ibiza","Nairobi","Juba")
# concatenating
print(k+y)
# checking length
if len (k)== len(y):
    print("lenghth is same")
else:
    print("Not the same")
# deleting a tuple
del k
print(k)