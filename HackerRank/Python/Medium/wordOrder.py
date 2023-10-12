n = int(input())
words = [input().strip() for _ in range(n)]

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


num_diferent_words = len(word_count)

occurrences = list(word_count.values())
print(num_diferent_words)
print(" ".join(map(str, occurrences)))
