import datetime
import csv
import os
import json

# this file is used for signal processing
class SignalProcessing:
    # temp_kept is the history of the sensor readings kept
    def __init__(self, comm_class, time_class, write_to_csv=True):
        # array to hold the datapoints in an array of (timestamp, signal)
        # array of points for each sensor
        # self.eye = []
        # self.body = []

        self.time_class = time_class

        self.comm_class = comm_class # communication class for grabbing signals from the comm class

        self.num_data_points = self.time_class.signal_data_point_num # number of discrete data points to keep in the running history

        # get json data to help
        json_data = json.load(open('params.json'))
        self.sensors = json_data["sensors"]

        # dictionary to hold the sensor data and initialize it
        self.sensor_data = {}
        for sensor_name in self.sensors:
            self.sensor_data[sensor_name] = []

        # csv information
        self.write_to_csv = write_to_csv
        dir = os.path.dirname(os.path.abspath(__file__))
        self.csv_save_path = dir + "/records/{}.csv".format(self.time_class.start_time)
        # write the first row as the columns
        data_row = [i for i in self.sensors]
        data_row.append("time")
        self.write_data_line(data_row)

    def get_body_classification(self):
        return False

    def get_eye_classification(self):
        return True

    def write_data_line(self, data_row):
        with open(self.csv_save_path, 'a', newline='') as csvfile:
            datawriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            datawriter.writerow(data_row)


    # update with a new datapoint taken from the comm class
    def update_with_new_datapoint(self):
        # check if the time is too far back
        current_time = self.time_class.get_time() # get the current time

        data_row = []
        # update each sensor
        for sensor_name in self.sensors:

            sensor_val = [self.comm_class.get_value(sensor_name), current_time]
            data_row.append(sensor_val[0])

            if len(self.sensor_data[sensor_name]) < self.num_data_points:
                self.sensor_data[sensor_name].append(sensor_val)
            else:
                # delete one point and add a new one
                del self.sensor_data[sensor_name][0]
                self.sensor_data[sensor_name].append(sensor_val)

        data_row.append(current_time)

        # write to csv if necessary
        if self.write_to_csv:
            self.write_data_line(data_row)
