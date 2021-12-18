from collections import deque

q = deque([1, 2, 3, 4, 5], 5)
q.append(6)  # 队尾进队
print(q.popleft())  # 队首出队

# 用于双向队列
q.appendleft(1)  # 队首进队
q.pop()  # 队尾出队