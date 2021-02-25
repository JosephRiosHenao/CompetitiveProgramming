# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
lista = set(input().split())
n2 = int(input())
lista2 = set(input().split())
print(len(lista.union(lista2)))
