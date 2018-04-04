# class to make sure everything is synched together
import time
import datetime

class TimerClass:
    # inverval for sampling rate, datapoints kept, state_interval_time
    def __init__(self, signal_interval, signal_history_window, state_interval, state_history_window):
        self.signal_interval  = signal_interval # time between data points taken
        self.signal_history_window = signal_history_window # time of the window history that we care about
        self.signal_data_point_num = self.signal_history_window // self.signal_interval

        self.state_interval = state_interval
        self.state_history_window = state_history_window
        self.state_data_point_num = self.state_history_window // self.state_interval

        self.start_time = datetime.datetime.now()
    def get_time(self):
        current_time = datetime.datetime.now() - self.start_time
        return current_time.total_seconds()
