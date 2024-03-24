import json
import csv
import os

class JSONExporter:
    def export_data(self, data, filename):
        with open(os.path.join('Exported Files', filename), 'w') as file:
            for item in data:
                json.dump(item, file, indent=2)
                file.write('\n')

class CSVExporter:
    def export_data(self, data, filename):
        with open(os.path.join('Exported Files', filename), 'w', newline='') as file:
            writer = csv.writer(file)
            for item in data:
                writer.writerow([item])
