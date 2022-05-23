""" Карта с населением трех стран Северной Америки
Pygal автоматически использует числа для окраски стран от светлых (менее населенные) до темных (наиболее населенные)
"""

import pygal

wm = pygal.maps.world.World()
wm.title = 'Население стран Северной Америки'
wm.add('Северная Америка', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')