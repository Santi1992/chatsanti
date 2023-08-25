import csv

class Csv ():

    def __init__ (self):
        pass

    def csv_to_list_of_dicts(self, file):
        result = []
        reader = csv.DictReader(file.read().decode('utf-8').splitlines())
        for row in reader:
            result.append(row)
        return result


