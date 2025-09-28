def chunks(lst, n):
    '''Работает как генератор и возвращает чанки массива lst размером n'''
    if not lst:
        yield []
    for i in range(0, len(lst), n):
        yield lst[i:i+n] # Index out of range в срезах lst[m:k] не появляется, python обрезает столько, сколько может

# Примеры использования
lst = [1,2,3,4,5,6,7,8,9,10]
print(f'List: {lst}')
for i, chunk in enumerate(chunks(lst, 5)):
    print(f'Chunk {i+1} = {chunk}')
print('')
# Chunk 1 = [1, 2, 3, 4, 5]
# Chunk 2 = [6, 7, 8, 9, 10]

lst = [1,2,3,4,5,6,7,8,9]
print(f'List: {lst}')
for i, chunk in enumerate(chunks(lst, 5)):
    print(f'Chunk {i+1} = {chunk}')
print('')
# Chunk 1 = [1, 2, 3, 4, 5]
# Chunk 2 = [6, 7, 8, 9]

lst = [1,2,3,4,5,6,7,8,9]
print(f'List: {lst}')
for i, chunk in enumerate(chunks(lst, 100)):
    print(f'Chunk {i+1} = {chunk}')
print('')
# Chunk 1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lst = []
print(f'List: {lst}')
for i, chunk in enumerate(chunks(lst, 10)):
    print(f'Chunk {i+1} = {chunk}')
# Chunk 1 = []