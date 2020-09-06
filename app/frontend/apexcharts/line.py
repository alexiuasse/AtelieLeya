#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 06/09/2020 10:15.

class Line:

    def __init__(self, x_title, y_title, series, colors, height=220, chart_type='area', stroke='smooth', title=""):
        self.title = title
        self.x_title = x_title
        self.y_title = y_title
        self.height = height
        self.stroke = stroke
        self.series = series
        self.chart_type = chart_type
        self.colors = colors

    def get_options(self):
        return {
            'series': self.series,
            'chart': {
                # 'defaultLocale': 'pt-br',
                # 'locales': self.get_locales(),
                'height': self.height,
                'type': self.chart_type,
                'zoom': {
                    'enabled': 0,
                }
            },
            'colors': self.colors,
            'dataLabels': {
                'enabled': 1,
            },
            'stroke': {
                'curve': self.stroke
            },
            'title': {
                'text': self.title,
                'align': 'left'
            },
            'grid': {
                'row': {
                    'colors': ['#f3f3f3', 'transparent'],
                    'opacity': 0.5,
                },
            },
            'xaxis': {
                'categories': ['Jan', 'Fev', 'Mar', 'Abr', 'Maio', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                'title': {
                    'text': self.x_title,
                }
            },
            'yaxis': {
                'title': {
                    'text': self.y_title
                },
            },
        }

    @staticmethod
    def get_locales():
        return [{
            'name': 'pt-br',
            'options': {
                'months': [
                    'Janeiro', 'Fevereiro', 'Março',
                    'Abril', 'Maio', 'Junho',
                    'Julho', 'Agosto', 'Setembro',
                    'Outubro', 'Novembro', 'Dezembro'
                ],
                'shortMonths': [
                    'Jan', 'Fev', 'Mar',
                    'Abr', 'Maio', 'Jun',
                    'Jul', 'Ago', 'Set',
                    'Out', 'Nov', 'Dez'
                ],
                'days': ['Sábado', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Domingo'],
                'shortDays': ['Sáb.', 'Seg.', 'Ter.', 'Qua.', 'Qui.', 'Sex.', 'Dom.'],
                'toolbar': {
                    'download': 'Baixar SVG',
                    'selection': 'Selecionar',
                    'selectionZoom': 'Selecionar Zoom',
                    'zoomIn': 'Zoom In',
                    'zoomOut': 'Zoom Out',
                    'pan': 'Panning',
                    'reset': 'Resetar Zoom',
                }
            }
        }]
