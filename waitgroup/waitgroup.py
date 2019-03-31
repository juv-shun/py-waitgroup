import multiprocessing as multi
import threading


class WaitGroupProcess():
    """WaitGroupProcess is like Go sync.WaitGroup for multiprocessing."""

    def __init__(self) -> None:
        self.count: multi.Value = multi.Value('d', 0)
        self.condition: multi.synchronize.Condition = multi.Condition()

    def add(self, n: int=1) -> None:
        with self.condition:
            self.count.value += n

    def done(self, n: int=1) -> None:
        with self.condition:
            self.count.value -= n
            if self.count.value == 0:
                self.condition.notify_all()

    def wait(self) -> None:
        with self.condition:
            while self.count.value > 0:
                self.condition.wait()


class WaitGroupThread():
    """WaitGroupProcess is like Go sync.WaitGroup for threading."""

    def __init__(self) -> None:
        self.count: int = 0
        self.condition: threading.Condition = threading.Condition()

    def add(self, n: int=1) -> None:
        with self.condition:
            self.count += n

    def done(self) -> None:
        with self.condition:
            self.count -= 1
            if self.count == 0:
                self.condition.notify_all()

    def wait(self) -> None:
        with self.condition:
            while self.count > 0:
                self.condition.wait()
