# VEXcode V5 Python - 4 Motor Arcade Drive
from vex import *

brain = Brain()
controller_1 = Controller(PRIMARY)

# --- Change ports & reversals to match your robot ---
left_front  = Motor(Ports.PORT11,  GearSetting.RATIO_18_1, False)
left_back   = Motor(Ports.PORT9,  GearSetting.RATIO_18_1, False)
right_front = Motor(Ports.PORT2,  GearSetting.RATIO_18_1, True)   # often reversed
right_back  = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)   # often reversed

# Group the sides so we can drive each side together
left  = MotorGroup(left_front, left_back)
right = MotorGroup(right_front, right_back)

# Smooth coasting when you let go
for m in (left_front, left_back, right_front, right_back):
    m.set_stopping(COAST)

deadband = 5  # ignore tiny stick noise (0–100)

while True:
    # Arcade drive
    fwd  = controller_1.axis3.position()   # forward/back
    turn = controller_1.axis1.position()   # left/right

    left_power  = fwd + turn
    right_power = fwd - turn

    # Deadband
    if abs(left_power) < deadband:   left_power = 0
    if abs(right_power) < deadband:  right_power = 0

    # Spin motor groups
    left.spin(FORWARD, left_power, PERCENT)
    right.spin(FORWARD, right_power, PERCENT)

    wait(10, MSEC)