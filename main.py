from signals import SignalProcessing
from timer_class import TimerClass
from comm import USBCommunication
from fsm import StateMachine

import time


# signal_interval, signal_history_window, state_interval, state_history_window in sec
timer_class = TimerClass(0.5, 10.0, 1.0, 100) # for timer data
fsm_class = StateMachine(timer_class) # for updating the stage of sleep

# create the comm class and start it to read values from the COM port
# set fake to false if you want to connect to the microcontroller
comm_class = USBCommunication('/dev/cu.usbmodem14611', 115200, fake=False, write_to_csv=True, delay=0.001)

# create the signal processing class to manage the comm data
# USBCommunication() class, SignalTimer() class
signal_class = SignalProcessing(comm_class, timer_class)

# updates for both the raw sensor readings and the fsm
sensor_update_last_time = timer_class.get_time()
fsm_update_last_time = timer_class.get_time()


# plotting help
import matplotlib.pyplot as plt
def plot_graph(array):
    plt.cla()
    plt.plot([x[1] for x in array], [y[0] for y in array])
    plt.draw()
    plt.pause(0.0001)

# start the while loop and update the sensor readings every interval
while True:

    current_time = timer_class.get_time()

    # sensor reading update loop
    if (current_time - sensor_update_last_time) >= timer_class.signal_interval:
        signal_class.update_with_new_datapoint() # update the sensor readings
        sensor_update_last_time = timer_class.get_time() # reset the last_update time

        # for key in signal_class.sensor_data:
        #     print("{}: {}".format(key, signal_class.sensor_data[key][-1]))

    # finite state machine update loop
    if (current_time - fsm_update_last_time) >= timer_class.state_interval:
        # update state with new data (body minute, eye minute)
        eye_classification = signal_class.get_eye_classification()
        body_classification = signal_class.get_body_classification()

        fsm_class.update_state(eye_classification, body_classification)
        fsm_update_last_time = timer_class.get_time()

        # print("Current State: {}".format(fsm_class.get_state()))

    time.sleep(.01)

    # this is used for plotting
    # plot_graph(signal_class.eye)
