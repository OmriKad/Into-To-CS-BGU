class s_queue:
    def __init__(self):
        self.s_queue_vals = []
        self.len = 0

    def enqueue(self, val):
        self.s_queue_vals.append(val)
        self.len += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('The queue is empty')
        tmp = self.s_queue_vals[0]
        self.s_queue_vals.pop(0)
        self.len -= 1
        return tmp

    def is_empty(self):
        if self.len == 0:
            return True
        else:
            return False

    def front(self):
        if self.is_empty():
            raise IndexError('The queue is empty')
        return self.s_queue_vals[0]

    def rear(self):
        if self.is_empty():
            raise IndexError('The queue is empty')
        return self.s_queue_vals[-1]

    def __len__(self):
        return self.len
