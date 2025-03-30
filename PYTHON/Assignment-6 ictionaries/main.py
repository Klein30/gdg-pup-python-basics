me ={
    "name": "James",
    "age": 19,
}
print("Original dictionary: ", me)
me.update({"city": "San Pedro"})
print("Dictionary after adding an item: ",me)
me.update({"age": 20})
print("Dictionary after updating an item: ", me)
me.pop("age")
print("Dictionary after removing an item: ",me)