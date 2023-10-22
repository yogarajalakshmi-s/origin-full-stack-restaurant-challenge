class OrderStateMachine:
    def __init__(self):
        self.state = "Submitted"
        self.transitions = {
            "Submitted": ["Approved", "Rejected", "Cancelled"],
            "Approved": ["In Preparation", "Cancelled"],
            "In Preparation": ["In Delivery"],
            "In Delivery": ["Delivered"],
            "Rejected": [],
            "Cancelled": [],
            "Delivered": [],
        }

    def transition(self, new_state):
        if new_state in self.transitions.get(self.state, []):
            self.state = new_state
            return self.state
        else:
            return "Invalid transition"
