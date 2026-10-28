
class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def mark_done(self):
        self.done = True
