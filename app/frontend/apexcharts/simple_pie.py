#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 03/09/2020 17:20.

class SimplePie:

    def __init__(self, labels, series, colors, width=360, chart_type='pie', title=""):
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
            'responsive': [{
                'breakpoint': 480,
                'options': {
                    'chart': {
                        'width': 300
                    },
                    'legend': {
                        'position': 'bottom'
                    }
                }
            }],
        }
