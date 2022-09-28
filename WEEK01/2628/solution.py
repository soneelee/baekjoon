w, h = map(int,input().split())
T = int(input())

row_idx = [0, h]
col_idx = [0, w]

for i in range(T):
    temp, idx = map(int,input().split())
    if temp == 0:
        row_idx.append(idx)
    else:
        col_idx.append(idx)

row_idx = sorted(row_idx)
col_idx = sorted(col_idx)

# print (row_idx)
# print (col_idx)

row_len = []
col_len = []
area = []

for i in range(len(row_idx)-1):
    row_len.append(row_idx[i+1] - row_idx[i])

for i in range(len(col_idx)-1):
    col_len.append(col_idx[i+1] - col_idx[i])

for i in range(len(row_len)):
    for j in range(len(col_len)):
        area.append(row_len[i]*col_len[j])

# print(row_len)
# print(col_len)
# print(area)

print(max(area))




