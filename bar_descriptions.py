# encoding=utf8
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#336699', base_style = LCS)
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
	{'value': 30084, "label": "Description of httpie."},
	{'value': 26306, "label": "Description of django."},
	{'value': 27670, "label": "Description of flask."}
	]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')