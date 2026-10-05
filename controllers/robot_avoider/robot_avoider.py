from controller import Robot, DistanceSensor, Motor


class AvoidRobot:
    def __init__(self):
        self.robot = Robot()
        self.time_step = int(self.robot.getBasicTimeStep())

        self.left_motor = self.robot.getMotor("left_motor")
        self.right_motor = self.robot.getMotor("right_motor")

        self.left_motor.setPosition(float('inf'))
        self.right_motor.setPosition(float('inf'))

        self.sensors = {}
        sensor_names = ["ds_front_left", "ds_front_right", "ds_left", "ds_right"]
        for name in sensor_names:
            sensor = self.robot.getDistanceSensor(name)
            sensor.enable(self.time_step)
            self.sensors[name] = sensor

        self.OBSTACLE_THRESHOLD = 320.0
        self.FORWARD_SPEED = 4.0
        self.TURN_SPEED = 3.2

    def get_sensor_reading(self):
        values = {}
        for name, sensor in self.sensors.items():
            values[name] = sensor.getValue()
        return values

    def run(self):
        while self.robot.step(self.time_step) != -1:
            readings = self.get_sensor_reading()

            front_min = min(readings["ds_front_left"], readings["ds_front_right"])
            left_value = readings["ds_left"]
            right_value = readings["ds_right"]

            if front_min < self.OBSTACLE_THRESHOLD or left_value < self.OBSTACLE_THRESHOLD or right_value < self.OBSTACLE_THRESHOLD:
                # The obstacle is close. Reverse and turn away from the side with the stronger reading.
                if right_value > left_value:
                    left_speed = self.TURN_SPEED
                    right_speed = -self.TURN_SPEED
                else:
                    left_speed = -self.TURN_SPEED
                    right_speed = self.TURN_SPEED
            else:
                left_speed = self.FORWARD_SPEED
                right_speed = self.FORWARD_SPEED

            self.left_motor.setVelocity(left_speed)
            self.right_motor.setVelocity(right_speed)


robot = AvoidRobot()
robot.run()
