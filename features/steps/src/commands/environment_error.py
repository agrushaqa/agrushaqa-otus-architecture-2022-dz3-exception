class TestEnvironmentError:
    def __init__(self, cmd, exception=""):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()
        raise OSError
