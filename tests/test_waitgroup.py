import multiprocessing as multi
import threading
import unittest

import waitgroup


class WaitGroupProcessTest(unittest.TestCase):
    def setUp(self):
        self.wg = waitgroup.WaitGroupProcess()

    def test_add(self):
        self.wg.add()
        self.assertEqual(self.wg.count.value, 1)
        self.wg.add()
        self.assertEqual(self.wg.count.value, 2)

    def test_done(self):
        self.wg.count.value = 10
        self.wg.done()
        self.assertEqual(self.wg.count.value, 9)
        self.wg.done()
        self.assertEqual(self.wg.count.value, 8)

    def test_wait(self):
        self.wg.count.value = 3
        multi.Process(target=self._decrease_count).start()
        self.wg.wait()
        self.assertEqual(self.wg.count.value, 0)

    def _decrease_count(self):
        import time
        time.sleep(2)
        with self.wg.condition:
            self.wg.count.value = 0
            self.wg.condition.notify_all()


class WaitGroupThreadTest(unittest.TestCase):
    def setUp(self):
        self.wg = waitgroup.WaitGroupThread()

    def test_add(self):
        self.wg.add()
        self.assertEqual(self.wg.count, 1)
        self.wg.add()
        self.assertEqual(self.wg.count, 2)

    def test_done(self):
        self.wg.count = 10
        self.wg.done()
        self.assertEqual(self.wg.count, 9)
        self.wg.done()
        self.assertEqual(self.wg.count, 8)

    def test_wait(self):
        self.wg.count = 3
        threading.Thread(target=self._decrease_count).start()
        self.wg.wait()
        self.assertEqual(self.wg.count, 0)

    def _decrease_count(self):
        import time
        time.sleep(2)
        with self.wg.condition:
            self.wg.count = 0
            self.wg.condition.notify_all()
