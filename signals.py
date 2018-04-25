import datetime
import csv
import os

# this file is used for signal processing
class SignalProcessing:
    # temp_kept is the history of the sensor readings kept
    def __init__(self, comm_class, time_class, write_to_csv=True):
        # array to hold the datapoints in an array of (timestamp, signal)
        # array of points for each sensor
        self.eye = []
        self.body = []

        self.time_class = time_class

        self.comm_class = comm_class # communication class for grabbing signals from the comm class

        self.num_data_points = self.time_class.signal_data_point_num # number of discrete data points to keep in the running history

        # csv information
        self.write_to_csv = write_to_csv
        dir = os.path.dirname(os.path.abspath(__file__))
        self.csv_save_path = dir + "/records/{}.csv".format(self.time_class.start_time)

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
        eye_val = [self.comm_class.get_value("acc_x"), current_time]
        body_val = [self.comm_class.get_value("acc_y"), current_time]

        # for the eye
        if len(self.eye) < self.num_data_points:
            self.eye.append(eye_val)
        else:
            # delete one point and add a new one
            del self.eye[0]
            self.eye.append(eye_val)

        # for the body
        if len(self.body) < self.num_data_points:
            self.body.append(body_val)
        else:
            # delete one point and add a new one
            del self.body[0]
            self.body.append(body_val)


        # write to csv if necessary
        if self.write_to_csv:
            self.write_data_line(eye_val)
