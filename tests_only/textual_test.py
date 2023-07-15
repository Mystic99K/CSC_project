import time
from textual.app import App

# Define Timer class
class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        return elapsed_time

# Define TimerApp
class TimerApp(App):
    view = None

    async def on_mount(self, event):
        await self.view.dock(header="Press 's' to start timer, 't' to stop timer")

    async def on_key(self, event):
        if event.key == "s":
            self.timer.start()
        elif event.key == "t":
            elapsed_time = self.timer.stop()
            await self.print(f"Elapsed time: {elapsed_time:0.4f} seconds")

    def __init__(self):
        super().__init__()
        self.timer = Timer()
        self.view = self.create_view()



# Run the app
app = TimerApp()
app.run()
