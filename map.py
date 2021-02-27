import setings as st

mapa = [
    '...................',
    '...................',
    '...................',
    '.##........##......',
    '...................',
    '...................',
    '...................',
]

inf_rect = []
for i in range(len(mapa)):
    for k in range(len(mapa[i])):
        if mapa[i][k] == '#':
            inf_rect.append([i + 20, k + 20, st.WIDTH, st.HEIGTH])