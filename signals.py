import datetime

# this file is used for signal processing
class SignalProcessing:
    # temp_kept is the history of the sensor readings kept
    def __init__(self, comm_class, time_class):
        # array to hold the datapoints in an array of (timestamp, signal)
        # array of points for each sensor
        self.eye = []
        self.body = []

        self.comm_class = comm_class # communication class for grabbing signals from the comm class

        self.interval = time_class.interval # time between data points taken
        self.history_window = time_class.history_window # time of the window history that we care about
        self.num_data_points self.history_window // self.interval # number of discrete data points to keep in the running history

    def get_body_classification(self):
        return True

    def get_eye_classification(self):
        return True

    # update with a new datapoint taken from the comm class
    def update_with_new_datapoint(self):
        # check if the time is too far back
        current_time = datetime.now() # get the current time
        eye_val = (self.comm_class.get_value("eye"), current_time)
        body_val = (self.comm_class.get_value("body"), current_time)

        # for the eye
        if len(self.eye) < self.num_data_points:
            self.eye.append(eye_val)
        else:
            # delete one point and add a new one
            del eye_val[0]
            self.eye.append(eye_val)

        # for the body
        if len(self.body) < self.num_data_points:
            self.body.append(body_val)
        else:
            # delete one point and add a new one
            del body_val[0]
            self.body.append(body_val)
