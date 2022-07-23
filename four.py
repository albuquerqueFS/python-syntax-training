parents, babies = (1, 1)
while babies < 100:
    print(f'This generation has {babies} babies')
    parents, babies = (babies, parents + babies)
    