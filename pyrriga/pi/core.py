import RPi.GPIO as gpio
import time
import logging

PIN_A = 23
PIN_B = 24


def gpio_setup():
    logging.info("Setting up GPIO to BCM")
    gpio.setmode(gpio.BCM)
    logging.info(f"Setting PIN_A ({PIN_A}) to OUT")
    gpio.setup(PIN_A, gpio.OUT)
    logging.info(f"Setting PIN_B ({PIN_B}) to OUT")
    gpio.setup(PIN_B, gpio.OUT)


def gpio_cleanup():  # free before exit
    logging.info(f"Cleanup GPIO")
    gpio.cleanup()


def start():
    logging.info("Opening valve")
    gpio.output(PIN_A, gpio.HIGH)
    gpio.output(PIN_B, gpio.LOW)
    time.sleep(1.5)
    gpio.output(PIN_A, gpio.HIGH)
    gpio.output(PIN_B, gpio.LOW)


def stop():
    logging.info("Closing valve")
    gpio.output(PIN_A, gpio.LOW)
    gpio.output(PIN_B, gpio.HIGH)
    time.sleep(1.5)
    gpio.output(PIN_A, gpio.LOW)
    gpio.output(PIN_B, gpio.HIGH)


def reset():
    logging.info("Reset relay status to OFF")
    gpio.output(PIN_A, gpio.LOW)
    gpio.output(PIN_B, gpio.LOW)
    time.sleep(1.5)
    gpio.output(PIN_A, gpio.LOW)
    gpio.output(PIN_B, gpio.LOW)
