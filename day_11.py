#add members
animal = {"Lion","Cat"}
print(animal)
animal.add("Dog")
print("Add single element : ",animal)
animal.update(["Ponda", "Tiger"])
print("Add multiple items : ",animal)

#remove
n = {30,50,70,20,30,60}
print("Before removing From Set :",n)
n.pop()
print("After removing From Set :",n)

#bonus
# Given sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Perform set operations
union_result = set_a.union(set_b)
intersection_result = set_a.intersection(set_b)
difference_result = set_a.difference(set_b)
symmetric_difference_result = set_a.symmetric_difference(set_b)

# Print results
print("1. Union:", union_result)
print("2. Intersection:", intersection_result)
print("3. Difference (set_a - set_b):", difference_result)
print("4. Symmetric Difference:", symmetric_difference_result)