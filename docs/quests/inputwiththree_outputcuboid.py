length, width, height = input().split()

L = int(length)
W = int(width)
H = int(height)

result = L*W*H

print("가로({})m * 세로({})m * 높이({})m = 직육면체{}m^3".format(L, W, H, result))
