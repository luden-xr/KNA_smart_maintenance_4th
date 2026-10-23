# print("-----실습1-----")

# data = [25, 26, 27, 28, 29]
# print(data)

# print(len(data))

# none = []
# print(len(none))


# print("-----실습2-----")

# data = [25, 26, 24, 28, 27]
# print(data[0])
# print(data[2])
# print(data[-1])

# print("-----실습3-----")

# data = [111, 234, 734, 732, 124, 111]
# x = data[0]
# y = data[-1]
# print( (x + y), ((x + y)/2) )

# print("-----실습4-----")

# data = [22,53,34,66,22,56,43,90,86,57]
# print(data[0:3])
# print(data[-3:])
# print(len(data[0:3]))
# print(len(data[-3:]))



# print("-----실습5-----")
# data = [1,2,3,4,5,6,7,8,9,10,11,12]
# first = data[:6]
# second = data[-6:]

# print(first)
# print(second)

# print(len(first))
# print(len(second))


# print("-----실습6-----")
# data = [22, 26, 29, 22, 32, 240]
# print(240 in data)
# data[5] = 24
# print(data)
# print(240 in data)



# print("-----실습7-----")
# data = []
# data.append(30)
# print(data)
# data.insert(0,28)
# print(data)
# data.extend([31,32])

# print(data)



# print("-----실습8-----")

# data= [24, 33, 34, 28, 999, 26]
# data.remove(999)
# print(data)
# removed = data.pop(4)
# print(removed)
# del data[1]
# print(data)

print("-----실습9-----")
data = [24, 34, 55, 27, 39, 30, 24, 27, 30, 27, 43, 27]
data.sort()
print(data)
data.reverse()
print(data)
print(data.count(27))
print(data.index(27))