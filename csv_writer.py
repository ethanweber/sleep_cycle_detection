import datetime

# this file is used for signal processing
class CSVWriter:
    # temp_kept is the history of the sensor readings kept
    def __init__(self, comm_class, time_class):
        # array to hold the datapoints in an array of (timestamp, signal)
        # array of points for each sensor
        self.eye = []
        self.body = []

        self.time_class = time_class

        self.comm_class = comm_class # communication class for grabbing signals from the comm class

        self.num_data_points = self.time_class.signal_data_point_num # number of discrete data points to keep in the running history

    def write_to_csv(self):
        
