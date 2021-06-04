# Python code to sort a list by creating another list Use of sorted()
def lensort(lst):
    lst2 = sorted(lst, key=len)
    return lst2
      
# code
lst = ["kaushal", "rahul", "dinesh", "nikhil", 
       "sumit", "umashanker", "deepak"]
print(lensort(lst))