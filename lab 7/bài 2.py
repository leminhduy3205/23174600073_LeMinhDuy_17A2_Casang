text = """My school garden
My school is situated near the most crowded market of the city. There is always rush of vehicles. But inside the school it is always fresh, thanks to the big and beautiful garden right at the entrance. School building starts after it. It has many trees, varieties of flowers and green grass. It is attached to the playground. We can sit in the garden in our recess period but playing is not allowed here. It filters the air of pollution and keeps our school’s environment cool and breathable. I love my school garden"""

words = text.split()
word_count = {word: words.count(word) for word in set(words)}

max_count = max(word_count.values())
min_count = min(word_count.values())

most_common_words = [word for word, count in word_count.items() if count == max_count]
least_common_words = [word for word, count in word_count.items() if count == min_count]

print("Từ có số lần xuất hiện nhiều nhất:")
for word in most_common_words:
    print(f"{word}: {max_count} lần")

print("\nTừ có số lần xuất hiện ít nhất:")
for word in least_common_words:
    print(f"{word}: {min_count} lần")
