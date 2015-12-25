import random, itertools, bisect

def randomtasks(tasks):
	population = [val for val, cnt in tasks for i in range(cnt)]
	return random.choice(population)

def randomtasks_bisect(tasks):
	choices, weights = zip(*tasks)
	cumdist = list(itertools.accumulate(weights))
	x = random.random() * cumdist[-1]
	return choices[bisect.bisect(cumdist, x)]

if __name__ == '__main__':
	tasks = [('CS', 8), ('Math', 4), ('Lang', 5), ('Sci', 2)]
	print(randomtasks_bisect(tasks))