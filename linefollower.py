from wpilib import DigitalInput


class LineFollower():
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain
        self.left_input = DigitalInput(8)
        self.right_input = DigitalInput(9)

    def run(self):
        print(f'Left: {self.left_input.get()}')
        print(f'Right: {self.right_input.get()}')
        # self.drivetrain.drive(0, 0.7)
        if self.left_input.get():
            self.drivetrain.drive(-0.5, -0.3)
        elif self.right_input.get():
            self.drivetrain.drive(0.5, -0.3)
        else:
            self.drivetrain.drive(0, -0.5)

