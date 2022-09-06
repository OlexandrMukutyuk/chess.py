cords = {'kingb': (5, 1), 'kingw': (5, 8), 'quineb': (4, 1), 'quinew': (4, 8),
         'ladia1w': (1, 8), 'ladia2w': (8, 8), 'ladia1b': (1, 1), 'ladia2b': (8, 1),
         'defender1w': (3, 8), 'defender2w': (6, 8), 'defender1b': (3, 1), 'defender2b': (6, 1),
         'horse1w': (2, 8), 'horse2w': (7, 8), 'horse1b': (2, 1), 'horse2b': (7, 1),
         'pawn1b': (1, 2), 'pawn2b': (2, 2), 'pawn3b': (3, 2), 'pawn4b': (4, 2),
         'pawn5b': (5, 2), 'pawn6b': (6, 2), 'pawn7b': (7, 2), 'pawn8b': (8, 2),
         'pawn1w': (1, 7), 'pawn2w': (2, 7), 'pawn3w': (3, 7), 'pawn4w': (4, 7),
         'pawn5w': (5, 7), 'pawn6w': (6, 7), 'pawn7w': (7, 7), 'pawn8w': (8, 7)
         }

cordb = {'kingb': cords['kingb'], 'quineb': cords['quineb'], 'ladia1b': cords['ladia1b'], 'ladia2b': cords['ladia2b'],
         'defender1b': cords['defender1b'], 'defender2b': cords['defender2b'],
         'horse1b': cords['horse1b'], 'horse2b': cords['horse2b'], 'pawn1b': cords['pawn1b'], 'pawn2b': cords['pawn2b'],
         'pawn3b': cords['pawn3b'], 'pawn4b': cords['pawn4b'],
         'pawn5b': cords['pawn5b'], 'pawn6b': cords['pawn6b'], 'pawn7b': cords['pawn7b'], 'pawn8b': cords['pawn8b']}
for item in cordb:
    print(item)