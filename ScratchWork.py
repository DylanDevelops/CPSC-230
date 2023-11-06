stop = 18
total = 0
for number in [5, 4, 6, 4, 6, 7]:
    print(number, end=' ')
    total += number
    if total > stop:
        print('*')
        break
else:
    print(f'/ {total}')
print('done')