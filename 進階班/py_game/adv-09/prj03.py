from collections import deque as dq

snack_queue = dq()
snack_queue.append("1")
snack_queue.append("2")
snack_queue.append("3")
print(snack_queue)
first = snack_queue.popleft()
print(first)
print(snack_queue)
snack_queue.append("0")
print(snack_queue)
