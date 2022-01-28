# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"Enemies inside function: {enemies}")
    
# increase_enemies()
# print(f"Enemies outside function: {enemies}")


# enemies2 = 1

# def increase_enemies():
#     enemies2 = 2
#     print(f"Enemies inside function: {enemies2}")
    
# increase_enemies()
# print(f"Enemies outside function: {enemies2}")


enemies = 1

def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies + 1
    
enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")