import time
import logging

PIN_A = 23
PIN_B = 24


def gpio_setup():
    logging.info("Setting up GPIO to BCM")

    logging.info(f"Setting PIN_A ({PIN_A}) to OUT")

    logging.info(f"Setting PIN_B ({PIN_B}) to OUT")


def gpio_cleanup():  # free before exit
    logging.info(f"Cleanup GPIO")


def start():
    logging.info("Opening valve")
    time.sleep(1.5)


def stop():
    logging.info("Closing valve")
    time.sleep(1.5)


def reset():
    logging.info("Reset relay status to OFF")
