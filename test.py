class MyClass:
    def __init__(self, value):
        self.value = value

    def example_function(self):
        print(f"This is an example function of object with value: {self.value}")

# Create a list to store instances of MyClass
objects_list = []

# Create instances of MyClass and add them to the list
for i in range(5):
    obj = MyClass(i)
    objects_list.append(obj)

# Accessing the function of the third instance in the list (index 2)
if len(objects_list) >= 3:  # Ensure the list has at least three elements
    third_obj = objects_list[2]
    third_obj.example_function()  # Calling the example function of the third object
else:
    print("There are not enough objects in the list to call the function of the third instance.")
