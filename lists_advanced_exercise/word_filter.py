words = [word for word in input().split(" ")]
filtered_words = [word for word in words if len(word)%2 == 0]
for word in filtered_words:
    print(word)