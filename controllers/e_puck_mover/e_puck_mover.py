import random
from controller import Robot, Motor


class EPUCKMover:
    def __init__(self):
        self.robot = Robot()
        self.time_step = int(self.robot.getBasicTimeStep())

        self.left_motor = self.robot.getMotor("left wheel motor")
        self.right_motor = self.robot.getMotor("right wheel motor")

        self.left_motor.setPosition(float('inf'))
        self.right_motor.setPosition(float('inf'))

        self.turn_timer = 0
        self.turn_direction = 1

    def run(self):
        while self.robot.step(self.time_step) != -1:
            if self.turn_timer > 0:
                self.turn_timer -= 1
                left_speed = self.turn_direction * 2.2
                right_speed = -self.turn_direction * 2.2
            else:
                left_speed = 4.5
                right_speed = 4.5

                if random.random() < 0.02:
                    self.turn_direction = 1 if random.random() > 0.5 else -1
                    self.turn_timer = random.randint(20, 60)

            self.left_motor.setVelocity(left_speed)
            self.right_motor.setVelocity(right_speed)


robot = EPUCKMover()
robot.run()
