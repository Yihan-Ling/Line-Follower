from wpilib import Spark
from wpilib.drive import DifferentialDrive


class Drivetrain:
    def __init__(self):
        self.left_motor = Spark(0)
        self.right_motor = Spark(1)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)

    def drive(self, rotate, forward):
        self.drivetrain.arcadeDrive(rotate, forward)