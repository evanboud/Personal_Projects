# Write a function `report` that takes any number of named
# gear counts and returns the TOTAL of all the values.

# ─────────────────────────────────────────────
# PRACTICE — DICTS + COMPREHENSIONS + LAMBDA
# ─────────────────────────────────────────────

# 1. Sort these by score, HIGHEST first.
#    hint: sorted has a `reverse=` argument
scores = [("alpha", 88), ("bravo", 92), ("charlie", 79)]
# expected: [("bravo", 92), ("alpha", 88), ("charlie", 79)]

x = sorted(scores, key= lambda item: item[1], reverse=True)
print(x)

# 2. Find the person with the highest score — return the whole pair.
scoresz = [("alpha", 88), ("bravo", 92), ("charlie", 79)]
# expected: ("bravo", 92)
x = sorted(scoresz, key= lambda item: item[1], reverse=True)
print(x[0])


# 3. Dict comprehension: build {name: score} from the list of pairs.
pairs = [("radio", 7), ("antenna", 2), ("cable", 5)]
# expected: {"radio": 7, "antenna": 2, "cable": 5}
res = dict(pairs)
print(res)
   
# 4. Tally — count each word. (you own this pattern now)
log = ["net", "radio", "net", "net", "radio"]
# expected: {"net": 3, "radio": 2}
items ={}
for item in log:
   items[item] = items.get(item, 0) + 1
print(items)




# 5. Sort a list of words by LENGTH, shortest first.
words = ["antenna", "net", "cable", "radio"]
# expected: ["net", "cable", "radio", "antenna"]
z = sorted(words, key= lambda word: len(word))
print(z)


# 6. Dict comprehension with a condition:
#    build a dict of ONLY the items with count > 4.
#    hint: comprehensions can end with an `if`
inventory = {"radio": 7, "antenna": 2, "cable": 5, "mount": 1}
# expected: {"radio": 7, "cable": 5}
pp = {key:value for key, value in inventory.item() if value > 4}
print(pp)
      
