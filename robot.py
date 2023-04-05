import wpilib
from wpilib import TimedRobot, Joystick, Spark
import os
from drivetrain import Drivetrain
from linefollower import LineFollower


class MyRobot(TimedRobot):
    def robotInit(self):
        self.drivetrain = Drivetrain()
        self.linefollower = LineFollower(self.drivetrain)

    def robotPeriodic(self):
        # This is called every cycle of the code. In general the code is loop through every .02 seconds.
        pass

    def autonomousInit(self):
        # This is called once when the robot enters autonomous mode.
        pass

    def autonomousPeriodic(self):
        # This is called every cycle while the robot is in autonomous.
        self.linefollower.run()

    def teleopInit(self):
        # This is called once at the start of Teleop.
        pass

    def teleopPeriodic(self):
        # This is called once every cycle during Teleop
        # forward = self.controller.getRawAxis(0)
        # rotate = self.controller.getRawAxis(1)
        # self.drivetrain.drive(forward, rotate)
        self.linefollower.run()

if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(MyRobot)
