from signals import SignalProcessing
from timer_class import SignalTimer
from comm import USBCommunication
from fsm import StateMachine



communcation = USBCommunication('COM1', 9600)

signal_timer = SignalTimer()
# time kept, SignalTimer() class to keep track of import data
signal_processor = SignalProcessing(100, signal_timer)
