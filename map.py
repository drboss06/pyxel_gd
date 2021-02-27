import setings as st

mapa = [
    '...................',
    '...................',
    '...................',
    '.##........##......',
    '...................',
]

inf_rect = []
for i in mapa:
    for k in i:
        if k == '#':
            inf_rect.append([i, k, st.WIDTH, st.HEIGTH])