# class to make sure everything is synched together
import time
import datatime

class TimerClass:
    # inverval for sampling rate, datapoints kept, state_interval_time
    def __init__(self, signal_interval, signal_history_window, state_interval, state_history_window):
        self.signal_interval # time between data points taken
        self.signal_history_window # time of the window history that we care about
        self.signal_data_point_num = self.signal_history_window // self.signal_interval

        self.state_interval = state_interval
        self.state_history_window = state_history_window
        self.state_data_point_num = self.state_history_window // self.state_interval


    def get_time():
        return datatime.now()
