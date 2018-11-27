import csv

DEFAULTVALUE = "None"


class CSVWriter:
    def __init__(self, data_set):
        self.data_set = data_set

    def write_file(self):
        with open('myData/combinedDataSet/finalDataSet.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(["ID", "Date", "Temperature 1", "Water1", "Temperature 2", "Water2"])
            for measurement in self.data_set:
                spamwriter.writerow([DEFAULTVALUE if measurement.id is None else measurement.id,
                                     measurement.datum,
                                     DEFAULTVALUE if measurement.temp_1 is None else measurement.temp_1,
                                     DEFAULTVALUE if measurement.water_1 is None else measurement.water_1,
                                     DEFAULTVALUE if measurement.temp_2 is None else measurement.temp_2,
                                     DEFAULTVALUE if measurement.water_2 is None else measurement.water_2])
