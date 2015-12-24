import random

def randomtasks(tasks):
	population = [val for val, cnt in tasks for i in range(cnt)]
	print(population)
	return random.choice(population)

if __name__ == '__main__':
	tasks = [('CS', 8), ('Math', 4), ('Lang', 5), ('Sci', 2)]
	print(randomtasks(tasks))