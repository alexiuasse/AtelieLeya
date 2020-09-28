#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/09/2020 14:41.

class SimplePie:

    def __init__(self, labels, series, colors, width=360, chart_type='donut', title=""):
        self.title = title
        self.labels = labels
        self.width = width
        self.series = series
        self.chart_type = chart_type
        self.colors = colors

    def get_options(self):
        return {
            'series': self.series,
            'chart': {
                'width': self.width,
                'type': self.chart_type,
            },
            'colors': self.colors,
            'labels': self.labels,
            'title': {
                'text': self.title,
                'align': 'left'
            },
            'legend': {
                'position': 'bottom'
            },
            'responsive': [{
                'breakpoint': 480,
                'options': {
                    'chart': {
                        'width': 300
                    },
                }
            }],
        }
