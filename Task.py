import datetime


class Task:
    def __init__(self, content):
        self.content = content
        self.date = str(datetime.datetime.now())[:-7]

    def __str__(self):
        return f"Task: '{self.content}' (created: {self.date})"

    def __repr__(self):
        return f"Task: '{self.content}' (created: {self.date})"

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.content == other.content
        return NotImplemented

    def __hash__(self):
        return hash(self.content)

    def __bool__(self):
        return bool(self.content)



