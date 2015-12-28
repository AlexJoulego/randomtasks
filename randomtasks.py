import random

def randomtasks(tasks):	
	population = [task for task in tasks for i in range(tasks[task])]
	return random.choice(population)


if __name__ == '__main__':
	tasks = {
		'CS': 8,
		'Math': 4,
		'Lang': 6,
		'Sci': 2
	}
	print(randomtasks(tasks))
