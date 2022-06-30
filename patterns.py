# arrow
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for image in picture:
    for pixel in image:
        if (pixel == 1):
            print('*', end='')
        else:
            print(' ', end='')   
    print('')         


# pattern 2
n = 5
for i in range(n):
    for j in range(i):
        print('*',end ='')
    print('')    

for i in range(n,0,-1):
    for j in range(i):
        print('*',end='')
    print('')

