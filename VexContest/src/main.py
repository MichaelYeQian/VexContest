from vex import *

# --- Initialize brain and controller ---
brain = Brain()
controller_1 = Controller(PRIMARY)

# --- Drive motors ---
left_front  = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
left_back   = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
right_front = Motor(Ports.PORT19, GearSetting.RATIO_18_1, True)
right_back  = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)

# Group each side
left_drive  = MotorGroup(left_front, left_back)
right_drive = MotorGroup(right_front, right_back)

# --- Extra motor (Port 1, counterclockwise) ---
extra_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)

# --- Settings ---
deadband = 5

# --- Main control loop ---
while True:
    # ---- Drive control ----
    forward = controller_1.axis3.position()
    turn = controller_1.axis1.position()

    left_speed  = forward + turn
    right_speed = forward - turn

    if abs(left_speed) < deadband:
        left_speed = 0
    if abs(right_speed) < deadband:
        right_speed = 0

    left_drive.spin(FORWARD, left_speed, PERCENT)
    right_drive.spin(FORWARD, right_speed, PERCENT)

    # ---- Spin motor control ----
    # Press R1 to spin counterclockwise
    if controller_1.buttonR1.pressing():
        extra_motor.spin(FORWARD, 100, PERCENT)
    else:
        extra_motor.stop()

    wait(10, MSEC)