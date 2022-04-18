class RadioDataset:
    def __init__(self, raw_data: list, labels_order: list, dataset_label: str = None):
        # dataset follows this pattern: {"label": value, ...}
        self.raw_data = raw_data
        self.dataset_label = dataset_label
        self.labels_order = labels_order

    def compute_data(self):
        data = []
        for label in self.labels_order:
            data.append(self.raw_data[label])
        return data

    def export(self):
        return {
            "label": self.dataset_label,
            'fill': True,
            "data": self.compute_data()
        }
