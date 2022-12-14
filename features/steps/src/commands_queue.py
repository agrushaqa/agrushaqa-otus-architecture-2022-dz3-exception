import queue

from src.exception_handler import exception_handler


class CommandsQueue:
    def __init__(self):
        self._running = True
        self.direct_queue = queue.Queue()

    def commands_worker(self):
        while True:
            try:
                cmd = self.direct_queue.get_nowait()
            except Exception:
                return  # exit from cycle when queue is empty
            self.direct_queue.task_done()
            try:
                cmd.execute()
            except Exception as ex:
                exception_handler(self.direct_queue, cmd, ex)

    def add_command(self, cmd):
        self.direct_queue.put(cmd)

    def wait_for_actual_termination(self):
        self.q.join()

    def stop(self):
        self._running = False
