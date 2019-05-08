__date__ = '2019/5/8 14:43'


class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while (len(self.queue)):
            if self.queue[0] + 3000 < t:
                self.queue.pop(0)
            else:
                break
        return len(self.queue)