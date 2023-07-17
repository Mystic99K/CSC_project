import time
import rich.live

def countdown(line, secs):
    with rich.live.Live() as live:
        for i in range(secs, 0, -1):
            live.update(f"{line} {i}")
            time.sleep(1)
