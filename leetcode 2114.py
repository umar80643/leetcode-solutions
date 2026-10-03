sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]


max_count = 0
for sentence in sentences:
    count = len(sentence.split())
    max_count = max(count, max_count)
print(max_count)
