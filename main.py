from signals import SignalProcessing
from timer_class import TimerClass
from comm import USBCommunication
from fsm import StateMachine

import time


# signal_interval, signal_history_window, state_interval, state_history_window in sec
timer_class = TimerClass(0.25, 1.0, 1.0, 100) # for timer data
fsm_class = StateMachine(timer_class) # for updating the stage of sleep

# create the comm class and start it to read values from the COM port
comm_class = USBCommunication('COM1', 9600, fake=True, write_to_csv=True)
# for microcontroller attachment
# comm_class.connect()
# comm_class.start()
# for fake data
# comm_class.start_fake_data_loop() # this runs in the background with fake data
# while True:
#     vals = comm_class.get_current_values()
#     print(vals)
#     time.sleep(.001)

# create the signal processing class to manage the comm data
# USBCommunication() class, SignalTimer() class
signal_class = SignalProcessing(comm_class, timer_class)

# updates for both the raw sensor readings and the fsm
sensor_update_last_time = timer_class.get_time()
fsm_update_last_time = timer_class.get_time()

# start the while loop and update the sensor readings every interval
while True:
    current_time = timer_class.get_time()

    # sensor reading update loop
    if (current_time - sensor_update_last_time) >= timer_class.signal_interval:
        signal_class.update_with_new_datapoint() # update the sensor readings
        sensor_update_last_time = timer_class.get_time() # reset the last_update time
    # print(len(signal_class.eye))
    print(signal_class.eye)
    # finite state machine update loop
    if (current_time - fsm_update_last_time) >= timer_class.state_interval:
        # update state with new data (body minute, eye minute)
        eye_classification = signal_class.get_eye_classification()
        body_classification = signal_class.get_body_classification()

        fsm_class.update_state(eye_classification, body_classification)
        fsm_update_last_time = timer_class.get_time()

        print("Current State: {}".format(fsm_class.get_state()))

    time.sleep(.025)
