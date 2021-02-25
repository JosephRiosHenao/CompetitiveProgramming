if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))
    
"""
if __name__ == '__main__':
    n = int(input())
    print(hash((tuple(map(int, input().split())))))
"""

#https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true