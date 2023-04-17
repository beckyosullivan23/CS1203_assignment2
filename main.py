from function23 import *
from my_Stack import *
from my_Queue import *

print(list_towns())
places = random_names(5)
print(places)

class my_Item:
    def __init__(self, name):
        self.name = name


places = [my_Item(name) for name in places]

# Create queue and add towns to it.
places_queue = my_Queue()
for item in places:
    places_queue.add(item)

# Create stack
places_stack = my_Stack()

# remove towns from the queue and add them to the stack
while not places_queue.empty():
    item = places_queue.remove()
    print(f"The location {item.name} has been removed from the queue.")
    places_stack.push(item)

# remove the towns from the stack.
while not places_stack.empty():
    item = places_stack.pop()
    print(f"The location {item.name} has been removed from the stack.")

print("You are now back home!")


