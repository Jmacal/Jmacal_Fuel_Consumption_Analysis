import os
import csv
from datetime import datetime

def extract_date(filename):
    date_str = filename.split('_')[1:5]
    date_str[3] = date_str[3][:-4]
    return datetime.strptime('_'.join(date_str), '%Y_%m_%d_%H%M')

def extract_columns(data_files, requested_columns):
    """
    Extracts specific columns from a log file and saves them in a CSV file.

    Args:
        data_filename (str): The name of the log file.
        requested_columns (list): A list of column names to extract from the log file.

    Raises:
        FileNotFoundError: If the log file does not exist.

    Returns:
        None
    """

    if all(f.endswith(".log") for f in data_files):

        sorted_data_files = sorted(data_files, key=extract_date)
    
        for data_filename in sorted_data_files:
            print(data_filename)

            data_file_dir = os.path.join('log_files', data_filename)
            
            if not os.path.isfile(data_file_dir):
                raise FileNotFoundError(f"{data_filename} does not exist.")
            else:
                with open(data_file_dir, 'r') as log_file:
                    log_data_generator = (log_row for log_row in log_file)

                    log_data = next(log_data_generator)

                    while not log_data.startswith('[column names]'):
                        log_data = next(log_data_generator)

                    column_names = next(log_data_generator).split(' ')

                    while not log_data.startswith('[data]'):
                        log_data = next(log_data_generator)


                    csv_file_dir = os.path.join('csv_files', data_filename[:-4] + '.csv')
                    n = 1
                    while os.path.isfile(csv_file_dir):
                        csv_file_dir = os.path.join('csv_files', data_filename[:-4] + f'__{n}.csv')
                        n += 1


                    with open(csv_file_dir, 'w') as csv_file:
                        csv_writer = csv.DictWriter(csv_file, fieldnames=requested_columns)
                        csv_writer.writeheader()
                        

                        for log_data in log_data_generator:
                            log_dict = dict(zip(column_names, log_data.split(' ')))

                            if 'Velocity' in requested_columns:
                                

                            csv_writer.writerow({column_name: log_dict[column_name] for column_name in requested_columns})


if __name__ == '__main__':
    log_files = os.listdir('log_files')
    extract_columns(log_files, ['time', 'NozGapOpen', 'NozGapClose', 'FanSpeed', 'EngineFuelRateTMSCS', 'TotalFuelConsumption', 'Velocity'])
