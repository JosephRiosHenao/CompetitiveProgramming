# Enter your code here. Read input from STDIN. Print output to STDOUT
listCountries = set()
n = int(input())
for _ in range(n):
    listCountries.add(input())
print(len(listCountries))
