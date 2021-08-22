from .cmd.helper import main

try:
    from .pi import core
except Exception:
    from .pi import fake_core as core
import time
import click
from rich.progress import Progress, Task


@main.command(help="Start the irrigation now")
@click.option("-d", "--duration", "duration", help="Duration in minutes", default="2", required=False, type=click.FLOAT)
def start(duration):
    core.gpio_setup()
    core.start()
    with Progress() as progress:
        task = progress.add_task(f"Irrigation in progress", total=int(duration * 60))
        for i in range(int(duration * 60)):
            time.sleep(1)
            progress.advance(task)
    core.stop()
    core.reset()


@main.command(help="Start the irrigation now")
def stop():
    core.gpio_setup()
    core.stop()
    core.reset()
