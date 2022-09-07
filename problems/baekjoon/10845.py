'''
    10845 - 큐, https://www.acmicpc.net/problem/10845

    input: n (1 <= n <= 10000)

    메모: 정답은 맞았는데 계속 시간초과가 떠서 class 부분을 구현한게 시간을 잡아먹나 싶었는데,
         빠른 입력을 사용해서 해결할 수 있었음. input() 대신 sys.stdin.readline() 사용.
'''
import sys

class Queue:
    def __init__(self, size) -> None:
        self.queue = [0] * size
        self.start = self.end = 0

    def push(self, x) -> None:
        self.queue[self.end] = x
        self.end += 1

    def pop(self) -> int:
        if self.start == self.end: 
            print(-1)
        else:
            print(self.queue[self.start])
            self.start += 1

    def size(self) -> None:
        print(self.end - self.start)
    
    def empty(self) -> None:
        if self.start == self.end:
            print(1)
        else:
            print(0)

    def front(self) -> None:
        if self.start == self.end:
            print(-1)
        else:
            print(self.queue[self.start])

    def back(self) -> None:
        if self.start == self.end:
            print(-1)
        else:
            print(self.queue[self.end - 1])
    

def main():
    n = int(sys.stdin.readline())
    q = Queue(n)

    for _ in range(n):
        command, *val = sys.stdin.readline().split()
        if command == 'push':
            q.push(int(val[0]))
        elif command == 'pop':
            q.pop()
        elif command == 'size':
            q.size()
        elif command == 'empty':
            q.empty()
        elif command == 'front':
            q.front()
        elif command == 'back':
            q.back()

    return

if __name__ == '__main__':
    main()