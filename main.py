from signals import SignalProcessing
from timer_class import TimerClass
from comm import USBCommunication
from fsm import StateMachine

import time


# signal_interval, signal_history_window, state_interval, state_history_window in sec
timer_class = TimerClass(0.25, 10.0, 1.0, 100) # for timer data
fsm_class = StateMachine(timer_class) # for updating the stage of sleep

# create the comm class and start it to read values from the COM port
# set fake to false if you want to connect to the microcontroller
comm_class = USBCommunication('COM1', 9600, fake=False, write_to_csv=True)

# create the signal processing class to manage the comm data
# USBCommunication() class, SignalTimer() class
signal_class = SignalProcessing(comm_class, timer_class)

# updates for both the raw sensor readings and the fsm
sensor_update_last_time = timer_class.get_time()
fsm_update_last_time = timer_class.get_time()


# get ready for plotting

import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random


# y = []
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
#
# def update(i):
#     yi = fun()
#     y.append(yi)
#     x = range(len(y))
#     ax.clear()
#     ax.plot(x, y)


def fun():
    if len(signal_class.eye) == 0:
        return 1
    else:
        return signal_class.eye[-1]

#
# def plot_cont(fun):
#     y = []
#     fig = plt.figure()
#     ax = fig.add_subplot(1,1,1)
#
#     def update(i):
#         yi = fun()
#         y.append(yi)
#         x = range(len(y))
#         ax.clear()
#         ax.plot(x, y)
#
#     a = anim.FuncAnimation(fig, update, repeat=False)
#     plt.draw()
#     plt.pause(0.01)
#
# plot_cont(fun)

import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
# plt.set_ylim((0,250))
plt.show(block=False)

# start the while loop and update the sensor readings every interval
while True:
    plt.pause(0.0001)

    current_time = timer_class.get_time()

    # sensor reading update loop
    if (current_time - sensor_update_last_time) >= timer_class.signal_interval:
        signal_class.update_with_new_datapoint() # update the sensor readings
        sensor_update_last_time = timer_class.get_time() # reset the last_update time
    # print(len(signal_class.eye))
    # print(signal_class.eye)
    # finite state machine update loop
    if (current_time - fsm_update_last_time) >= timer_class.state_interval:
        # update state with new data (body minute, eye minute)
        eye_classification = signal_class.get_eye_classification()
        body_classification = signal_class.get_body_classification()

        fsm_class.update_state(eye_classification, body_classification)
        fsm_update_last_time = timer_class.get_time()

        print("Current State: {}".format(fsm_class.get_state()))


    time.sleep(.025)
    plt.cla()
    plt.plot([x[1] for x in signal_class.eye], [y[0] for y in signal_class.eye])
    plt.draw()
