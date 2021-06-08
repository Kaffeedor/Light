from apa102_pi.driver import apa102
import time

NUM_LED = 111

strip = apa102.APA102(num_led=NUM_LED, order="rgb")



