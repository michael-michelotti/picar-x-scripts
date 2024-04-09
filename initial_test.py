from robot_hat.utils import reset_mcu
from picarx import Picarx
from vilib import Vilib
import time
import readchar


px = Picarx()


def main():
    speed = 0
    status = 'stop'

    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)
    time.sleep(2)

    for angle in range(0, 35):
        px.set_dir_servo_angle(angle)
        time.sleep(0.01)
    for angle in range(35, -35, -1):
        px.set_dir_servo_angle(angle)
        time.sleep(0.01)
    for angle in range(-35, 0):
        px.set_dir_servo_angle(angle)
        time.sleep(0.01)

    while True:
        key = readchar.readkey().lower()
        print(key)
        time.sleep(0.1)


try:
    main()
except:
    print("error")
finally:
    px.stop()
    Vilib.camera_close()
