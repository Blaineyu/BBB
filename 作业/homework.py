#基础作业

#1.1
type(1.1)
type(5)

#1.2
a = 3
b = 4
c = 5
print(a+b+c)
print(a==b) 

#1.3
a = input('Please enter a number in [1,100]:')
while True:    
    try:
        if 1 <= float(a) <=100:
            print('100以内的数字',a)
            break
        else:
            print('区间以外的数字')
            a=input('Please enter a number in [1,100]:')
    except:
        print('incorrect form')
        a=input('Please enter a number in [1,100]:')

#1.4
# 这是单行注释 

'''
这是多行注释
这是多行注释
这是多行注释
'''


# 进阶作业

#2.1
counter = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i !=j and j !=k and k !=i:
                print('{}{}{}'.format(i,j,k),end=' ')
                counter +=1
print('')
print('共{}种组合'.format(counter))

#2.2
a = [1, 2, 3, 4, 5]
Answer_1 = a[::2]
Answer_2 = a[-2:]
print(Answer_1)
print(Answer_2)

#2.3
def is_odd(n):
    return  n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))



