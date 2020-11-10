###############################################################
###############################################################
## This code is for formatting the hrm file                  ##
## To run this code use the following command:               ##
## python main.py "path_to_csv_file" "name_for_new_file"     ##
###############################################################
###############################################################

import os
import sys
from datetime import datetime

import pandas as pd


def is_file_not_empty(file):
    if os.fstat(file.fileno()).st_size > 0:
        return True
    else:
        return False


def check_the_file(file_url, new_filename):
    if file_url is not False:
        f = open(file_url, 'r')
        if is_file_not_empty(f):
            create_new_reformatted_file(file_url, new_filename)
        else:
            print("The file is empty")
        f.close()
    else:
        print("The path to the file is wrong")


def create_new_reformatted_file(file_url, new_filename):
    print("Reformatting started...")
    old_dataframe = pd.read_csv(file_url)
    convert_timestamp_to_datetime(old_dataframe)
    new_dataframe = pd.DataFrame(old_dataframe, columns=['username_id', 'time', 'value'])
    # new_dataframe.rename(columns={"username_id": "Username", "timestamp": "Timestamp", "value": "Heart rate"})
    new_dataframe.to_csv(new_filename, index=False, header=True)
    print("Successfully finished...")


def convert_timestamp_to_datetime(dataframe):
    datetime_array = []
    for item, value in dataframe['timestamp'].iteritems():
        datetime_array.append(datetime.fromtimestamp(value/1000))
    dataframe['time'] = datetime_array
    return dataframe


def main(argv):
    files_url = argv[0]
    new_file_name = argv[1]
    check_the_file(files_url, new_file_name)
    print(argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
