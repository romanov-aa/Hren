'''
a = 10
b = 20
if a == b:
    print("a > b")
    if b is True:
        print("True")
elif a < b:
    print('a < b')
elif a != b:
    pass
else:
    print("a = b")

# Список [], кортедж ()
n = [1, 2, 3, 'sorry']
# for i in n:
#     print(i)
print(len(n))
n.append(7)
print(n)
'''
# while True: + равно бесконечный цикл
m = 0
while m < 10:
    print(m)
    m += 1
