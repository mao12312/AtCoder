# n = int(input())
# card_list = [
#     "S 1", "S 2", "S 3", "S 4", "S 5", "S 6", "S 7", "S 8", "S 9", "S 10", "S 11", "S 12", "S 13",
#     "H 1", "H 2", "H 3", "H 4", "H 5", "H 6", "H 7", "H 8", "H 9", "H 10", "H 11", "H 12", "H 13",
#     "C 1", "C 2", "C 3", "C 4", "C 5", "C 6", "C 7", "C 8", "C 9", "C 10", "C 11", "C 12", "C 13",
#     "D 1", "D 2", "D 3", "D 4", "D 5", "D 6", "D 7", "D 8", "D 9", "D 10", "D 11", "D 12", "D 13"
# ]
# # arr = list(set(card_list)-set(['S 1', 'S 2']))
# # arr2 = sorted(arr)
# # # print(arr)
# have_list = []
# for i in range(n):
#     inpt = input()
#     have_list.append(inpt)

# for i in card_list:
#     for j in have_list:
#         if i == j:
#             card_list.remove(j)
# print(have_list)
# print(card_list)
# # for j in ans:
# #     print(j, end='\n')


n = int(input())
c = {
    'S': [0]*13,
    'H': [0]*13,
    'C': [0]*13,
    'D': [0]*13
}
for i in range(n):
    s, num = input().split()
    c[s][int(num)-1] = 1

for i in ["S", 'H', 'C', 'D']:
    for j in range(13):
        if c[i][j] == 0:
            print(i, j+1)
