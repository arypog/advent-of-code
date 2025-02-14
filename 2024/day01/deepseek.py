def calculate_total_distance(left, right):
    left_sorted = sorted(left)
    right_sorted = sorted(right)
    total = 0
    for i in range(len(left_sorted)):
        total += abs(left_sorted[i] - right_sorted[i])
    return total

from collections import Counter

def calculate_similarity_score(left, right):
    counter_right = Counter(right)
    total = 0
    for num in left:
        count = counter_right.get(num, 0)
        total += num * count
    return total

# Read input (assuming standard input format as per problem statement)
left = []
right = []

path = 'in/in.pub'
with open(path, 'r') as f: 
    for line in f:
       parts = line.strip().split(' ')
       left.append(int(parts[0]))
       right.append(int(parts[-1]))

# Compute and print results for both parts
print("Total Manhattan Distance:", calculate_total_distance(left, right))
print("Similarity Score:", calculate_similarity_score(left, right))