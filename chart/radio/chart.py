import json

from chart.radio.dataset import RadioDataset


class RadioChart:
    def __init__(self, raw_data):
        # raw_data follows this pattern: {dataset_label: dataset, ...}
        # dataset follows this pattern: {label: value, ...}
        self.raw_data = raw_data
        self.labels = self.compute_labels()

    def compute_labels(self):
        for dataset_label in self.raw_data:
            return list(self.raw_data[dataset_label].keys())

    def generate_dataset(self):
        dataset_list = []
        for dataset_label, raw_dataset in self.raw_data.items():
            dataset = RadioDataset(
                raw_data=raw_dataset,
                dataset_label=dataset_label,
                labels_order=self.labels
            )
            dataset_list.append(
                dataset.export()
            )
        return dataset_list

    def export_chart(self):
        print({
            "type": 'radar',
            "data": {
                "labels": self.labels,
                "datasets": self.generate_dataset()
            }
        })
        return json.dumps({
            "type": 'radar',
            "data": {
                "labels": self.labels,
                "datasets": self.generate_dataset()
            }
        })
