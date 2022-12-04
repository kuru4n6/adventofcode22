# Setup

with open('input', 'r') as handle:
    calories = handle.read().split('\n\n')

# Part 1
max_calories = max([sum(list(map(int, calories_per_elve.split('\n')))) for calories_per_elve in calories])
print(max_calories)

# Part 2
calories_list = [sum(list(map(int, calories_per_elve.split('\n')))) for calories_per_elve in calories]
calories_list.sort(reverse=True)
top_three_elves = sum(calories_list[:3])
print(top_three_elves)
