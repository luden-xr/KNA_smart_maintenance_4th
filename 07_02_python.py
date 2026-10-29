# print("------실습2------")
# def start(name, data):
#     print(f'{name}{data}도')

# start('모터', 78)
# start('펌프', 92)

# start(78, '모터')
# start(92, '펌프')

# print("-----실습3-----")
# def start(name, data):
#     print(f'{name} {data}')

# start(data=78, name="모터")
# start("펌프", 92)

# print("-----실습4-----")
# def start(x,y):
#     return (x+y)/2
# avg = start(80,90)
# print(avg)
# print(avg + 5)


print("-----실습5-----")
def data(values):
    return min(values), max(values), sum(values)/len(values)
value = [78,92,85]
x,y,z = data(value)
print(x, y, z)