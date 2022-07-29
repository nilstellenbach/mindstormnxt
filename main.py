import time

import nxt.motcont
import nxt.motor as nxt.motor

    def wait():
        while not mc.is_ready(nxt.motor.Port.A):
            time.sleep(0.5)

    mc.start()

    mc.cmd((nxt.motor.Port.A), 50)
    wait()

    mc.cmd((nxt.motor.Port.A), -50)
    wait()

    mc.stop()