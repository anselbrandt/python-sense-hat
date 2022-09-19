from sense_hat import SenseHat
import logging

logging.getLogger().setLevel(logging.ERROR)
sense = SenseHat()

temp = sense.temp
press = sense.pressure
orient = sense.orientation
comp = sense.compass
gyro = sense.gyro
accel = sense.accel

print(f"temp {temp}\npressure {press}\norientation {orient}\ncompass {comp}\ngyro {gyro}\naccel {accel}\n")
