listy = [1,2,3,1,2,3,1,2,3]

for i in listy:
    print(f'got {i}')
    if i == 2:
        print('nexting')
        next
    if i == 3:
        print('continuing')
        continue
    
    print(f'end {i}')