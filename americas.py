""" Простая карта с данными по Северной, Центральной и Южной Америке """
import pygal

wm = pygal.maps.world.World()
wm.title = 'Северная, Центральная, и Южная Америки'

wm.add('Северная Америка', ['ca', 'mx', 'us'])
wm.add('Центральная Америка', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('Южная Америка', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('americas.svg')