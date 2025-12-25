raw_input = open("./input.txt", "r+").read()

ordering_rules, updates = raw_input.split("\n\n")
ordering_rules = ordering_rules.split("\n")
updates = updates.split("\n")
for i in range(len(updates)): updates[i] = [int(n) for n in updates[i].split(",")]

ordering_map = {}
for ordering in ordering_rules:
    later, earlier = [int(n) for n in ordering.split("|")]
    if earlier in ordering_map: ordering_map[earlier].add(later)
    else: ordering_map[earlier] = {later}
  
# Part 1  
# total = 0
    
# for update in updates:
#     correct = True
#     for i in range(len(update)):
#         page = update[i]
#         for j in range(0, i):
#             prev_page = update[j]
#             if prev_page in ordering_map and page in ordering_map[prev_page]:
#                 correct = False
#                 break
#         if not correct: break
#     if correct:
#         total += update[len(update) // 2]
        
# print(total)

# Part 2
# total = 0

# for update in updates:
#     incorrect = False
#     for i in range(len(update)):
#         page = update[i]
#         j = 0
#         while j < i:
#             prev_page = update[j]
#             if prev_page in ordering_map and page in ordering_map[prev_page]:
#                 update[j] = page
#                 update[i] = prev_page
#                 page = update[i]
#                 j = 0
#                 incorrect = True
#             else: j += 1
#     if incorrect: total += update[len(update) // 2]

# print(total)
