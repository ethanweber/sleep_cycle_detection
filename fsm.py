# this code consists of our finite state machine for sleep stage detection

class StateMachine:
    def __init__(self, timer_class):
        self.current_state = "wake" # start as awake by default
        # self.states = {"wake", "nrem", "rem"}
        self.state_history_length = timer_class.state_data_point_num
        self.state_history = []

        # thresholds in percentage
        # if body_mov_count > wake percentage then we are wake, otherwise sleeping
        self.wake_thresh = 0.5

        self.rem_eye_thresh = 0.5

        # store the previous state to know where we are coming from
        self.previous_state = None

    def get_state(self):
        return self.current_state
    def update_state(self, eye_classification, body_classification):
        #TODO use these inputs to update the state (wake, nrem, rem) based on history

        # first add new state to the history
        new_state = [eye_classification, body_classification]
        if len(self.state_history) < self.state_history_length:
            self.state_history.append(new_state)
        else:
            # delete one point and add a new one
            del self.state_history[0]
            self.eye.append(new_state)


        # check if woken up and get the number of states in history
        body_mov_per = 0
        eye_mov_per = 0
        for i in self.state_history:
            if i[1] == True: body_mov_per += 1.0
            if i[0] == True: eye_mov_per += 1.0
        body_mov_per = body_mov_per / len(self.state_history)
        eye_mov_per = eye_mov_per / len(self.state_history)

        if self.current_state == "wake":
            # check if going to "nrem" (going to sleep)
            if body_mov_per < self.wake_thresh:
                self.previous_state = "wake"
                self.current_state = "nrem"

        elif self.current_state == "nrem":

            # check if going to "wake"
            if body_mov_per > self.wake_thresh:
                self.previous_state = "nrem"
                self.current_state = "wake"

            # check if going to "rem"
            elif eye_mov_per > self.rem_eye_thresh:
                self.previous_state = "nrem"
                self.current_state = "rem"


        elif self.current_state == "rem":

            # check if going to "wake"
            if body_mov_per > self.wake_thresh:
                self.previous_state = "rem"
                self.current_state = "wake"
            # else check if going back to "nrem"
            elif eye_mov_per < self.rem_eye_thresh:
                self.previous_state = "rem"
                self.current_state = "nrem"

        else:
            # TODO throw an error because there must be a state
            pass
