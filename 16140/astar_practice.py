# trying to get all the N-digit binary numbers
# https://www.youtube.com/watch?v=hettiSrJjM4 -> Modified BFS

import queue


def printQueue(q: queue):
	print(list(q.queue))
	# while not q.empty():
		# print(q.get())

q = queue.Queue()
q.put("")

for _ in range(8):
	# temp = []
	# while not q.empty():
	x = q.get()
	# temp.append(x+'0')
	# temp.append(x+'1')
	# for x in temp:
		# q.put(x)
	# x = q.get()
	# y = x + '0'
	# z = x + '1'
	q.put(x+'0')
	q.put(x+'1')
	# q.put(y)
	# q.put(z)
	printQueue(q)
	print("#"*40)
	
print( 0 < 5 < 6)