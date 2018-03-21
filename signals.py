# this file is used for signal processing

class SignalProcessing:
    # temp_kept is the history of the sensor readings kept
    # take the timer class to keep track of the time
    def __init__(self, time_kept, timer_class):
        # array to hold the datapoints in an array of (timestamp, signal)
        # array of points for each sensor
        self.sensor1 = []
        self.sensor2 = []
        self.sensor3 = []
        self.time_kept = time_kept

    def get_body_movement(self):
        return True
    def get_body_movement(self):
        return True
    def get_body_movement(self):
        return True
    def add_reading(self, point):
        # check if the time is too far back
        if self.sensor1[0][0]
