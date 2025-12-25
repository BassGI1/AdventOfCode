disk_map = open("./input.txt").read()

# Part 1
# disk = []
# latest_id = 0

# for i in range(len(disk_map)):
#     current_file = int(disk_map[i])
#     if i % 2:
#         for _ in range(current_file): disk.append(".")
#     else:
#         for _ in range(current_file): disk.append(latest_id)
#         latest_id += 1
        
# left, right = 0, len(disk) - 1

# while left < right:
#     while disk[left] != ".": left += 1
#     while disk[right] == ".": right -=1
#     if left < right:
#         temp = disk[left]
#         disk[left] = disk[right]
#         disk[right] = temp
        
# checksum = 0
# for i in range(len(disk)):
#     if disk[i] == ".": break
#     checksum += i*(disk[i])
        
# print(checksum)

# Part 2
# class Block:
#     def __init__(self, id, size):
#         self.id = id
#         self.size = size
        
#     def __str__(self):
#         return (f"{self.id if self.id != -1 else '.'}")*self.size
    
#     def checksum(self, start):
#         total = 0
#         for i in range(self.size):
#             total += (start + i)*self.id
#         return total
        
# disk = list[Block]()
# latest_id = 0

# for i in range(len(disk_map)):
#     current_file = int(disk_map[i])
#     if i % 2: disk.append(Block(-1, current_file))
#     else:
#         disk.append(Block(latest_id, current_file))
#         latest_id += 1
        
# for i in range(len(disk) - 1, -1, -1):
#     if disk[i].id != -1:
#         for j in range(i):
#             if disk[j].id == -1 and disk[i].size == disk[j].size:
#                 temp = disk[i]
#                 disk[i] = disk[j]
#                 disk[j] = temp
#                 break
#             elif disk[j].id == -1 and disk[i].size < disk[j].size:
#                 fragment_size = disk[j].size - disk[i].size
#                 disk[j].size = disk[i].size
#                 temp = disk[j]
#                 disk[j] = disk[i]
#                 disk[i] = temp
#                 disk = disk[:j + 1] + [Block(-1, fragment_size)] + disk[j + 1:]
#                 break
            
# index = 0
# checksum = 0
# for block in disk:
#     if block.id != -1:
#         checksum += block.checksum(index)
#     index += block.size
    
# print(checksum)