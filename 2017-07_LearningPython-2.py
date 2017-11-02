# Programming Foundations: Real-World Examples - Barron Stone _ Lynda.com

def mix_and_cook():
	print('Mixing the ingredients')
	print('Greasing the frying pan')
	print('Pouring the mixture into a frying pan')
	print('Cooking the first side')
	print('Flipping it!')
	print('Cooking the other side')

# def make_omelette():
# 	mix_and_cook()
# 	omelette = 'a tasty omelette'
# 	return omelette 

def make_omelette(ingredient):
	mix_and_cook()
	omelette = 'a {} omelette' .format(ingredient)
	return omelette 

def fancy_omelette(*ingredients):
	mix_and_cook()
	omelette = 'a fancy omelette with {} ingredients' .format(len(ingredients))
	return omelette 

def make_pancake():
	mix_and_cook()
	pancake = 'a delicious pancake'
	return pancake

# print(make_omelette())
# print(make_pancake())

# print(make_omelette('bacon'))

print(fancy_omelette('sausage','onion','pepper','spinach','mushroom'
	,'tomato','goat cheese'))

## Functions search for variables locally first. 
## If the variable is not in the local scope, it expands the search to the global scope.

# When a method is called on an object, Python automatically passes that object as the first argument.
# Self provides a convenient way to access and modify an object within a method. 


# Mutable object can be modified after it's been created; an immutable object cannot 
# Plus operator creates a new string containing the concatenated phrase, and binds the new object to the name words



























