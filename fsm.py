# this code consists of our finite state machine for sleep stage detection

class StateMachine:
    def __init__(self, timer_class):
        self.current_state = None
        self.state_history_length = state_history_length
        self.state_history = []
    def get_state():
        return self.current_state
    def update_state(eye_classification, body_classification):
        #TODO use these inputs to update the state (wake, nrem, rem) based on history
        pass
