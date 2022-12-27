class TodoList:
    def __init__(self, size=2):
        self.tasks = [None] * (size+1)

    def __setitem__(self, key, value):
        self.tasks[key] = value

    def __getitem__(self, item):
        return self.tasks[item]

    def __delitem__(self, key):
        del self.tasks[key]

    def __iter__(self):
        self.value = self.tasks[0]
        return self

    def __next__(self):
        try:
            self.value
        except AttributeError:
            self.value = self.tasks[0]
        placing = self.tasks.index(self.value)
        if placing < len(self.tasks)-1:
            out = self.value
            self.value = self.tasks[placing+1]
            return out
        else:
            raise StopIteration
