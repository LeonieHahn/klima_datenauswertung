from combine_data import DataParser
from csv_writer import CSVWriter
import glob


def main():
    # select all csvs from myData
    my_csv = glob.glob("myData/*.csv")
    data_set_complete = []
    my_parser = DataParser()

    # create one big list will all measurements
    for csv_file in my_csv:
        my_parser.pass_file(csv_file)
        data_set_complete += my_parser.import_one_csv()

    # sort by date does not work yet as there appear dates multiple times
    data_set_complete.sort(key=lambda x: x.datum)

    my_parser.set_full_data_set(data_set_complete)  # pass the list to the parser

    data_set_complete = my_parser.fill_missing_dates()

    # write one big csv-file
    csv_writer = CSVWriter(data_set_complete)
    csv_writer.write_file()


if __name__ == "__main__":
    main()
