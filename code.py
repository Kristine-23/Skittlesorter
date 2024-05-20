import board
import busio
import time
import pwmio
from adafruit_motor import servo
import adafruit_tcs34725


pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)
pwm1 = pwmio.PWMOut(board.GP17, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)
my_servo1 = servo.Servo(pwm1)

##################
# *EDIT*
# Set configurable values below
# Feed name for Adafruit IO

# milliseconds to gather color data
sensor_integration_time = 150

# manually override the color sensor gain
sensor_gain = 4

# Collect this many samples each time we prompt the user
num_samples = 5


# Create sensor object, communicating over the board's default I2C bus
i2c = busio.I2C(board.GP15, board.GP14)  # uses first I2C SCA/SCL pair on pico
sensor = adafruit_tcs34725.TCS34725(i2c)

# Change sensor gain to 1, 4, 16, or 60
sensor.gain = sensor_gain
# Change sensor integration time to values between 2.4 and 614.4 milliseconds
sensor.integration_time = sensor_integration_time


def Red():
    pwm1.angle = 0


def Orange():
    pwm1.angle = 0


def Yellow():
    pwm1.angle = 0


def Green():
    pwm1.angle = 0


def Purple():
    pwm1.angle = 0


while True:
    my_servo.angle = 90
    time.sleep(3)
    print(sensor.color_rgb_bytes)
    red = sensor.color_rgb_bytes[0]
    green = sensor.color_rgb_bytes[1]
    blue = sensor.color_rgb_bytes[2]
    color_detected = False
    if red < 45 and red > 21 and green > 10 and green < 17 and blue < 8:
        print("red detected")
        color_detected = True
        my_servo1.angle = 165
    else:
        print("nothing detected")

    if red > 35 and red < 76 and green > 5 and green < 13 and blue < 4:
        print("orange detected")
        color_detected = True
        my_servo1.angle = 140
    else:
        print("nothing detected")

    if red <= 34 and red > 20 and green > 17 and green < 25 and blue < 3:
        print("yellow detected")
        color_detected = True
        my_servo1.angle = 115
    else:
        print("nothing detected")

    if red > 10 and red < 15 and green > 27 and green < 38 and blue <= 5:
        print("green detected")
        color_detected = True
        my_servo1.angle = 85
    else:
        print("nothing detected")

    if red > 13 and red < 23 and green > 15 and green < 23 and blue < 10:
        print("purple detected")
        color_detected = True
        my_servo1.angle = 65
    else:
        print("nothing detected")

    time.sleep(1)
    print("Temperature: %d" % sensor.color_temperature)
    print(
        "r: %d, g: %d, b: %d"
        % (
            sensor.color_rgb_bytes[0],
            sensor.color_rgb_bytes[1],
            sensor.color_rgb_bytes[2],
        )
    )
    print("Lux: %d" % sensor.lux)  # Write your code here :-)
    if color_detected == True:
        my_servo.angle = 0 #drop the skittle
        time.sleep(3)
        my_servo.angle = 180 #grab the skittle
        time.sleep(3)
    my_servo1.angle = 115
    print("servo1 moving")
    time.sleep(5)
    my_servo1.angle = 65
    print("servo1 moving")
    time.sleep(2)
