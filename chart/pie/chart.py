import json

from chart.color.color_picker import ColorPicker


class PieChart:
    def __init__(self, raw_data):
        # raw_data follows this pattern: {label: value, ...}
        self.raw_data = raw_data
        self.labels = self.compute_labels()
        self.colors = self.generate_colors()
        self.data = self.generate_data()

    def compute_labels(self):
        return list(self.raw_data.keys())

    def generate_colors(self):
        colors = []
        for index in range(len(self.labels)):
            colors.append(ColorPicker.get_color(index))
        return colors

    def generate_data(self):
        data = []
        for label in self.labels:
            data.append(self.raw_data[label])
        return data

    def generate_dataset(self):
        return [{
          "data": self.data,
          "backgroundColor": self.colors
        }]

    def export_chart(self):
        return json.dumps({
            "type": 'pie',
            "data": {
                "labels": self.labels,
                "datasets": self.generate_dataset()
            }
        })
