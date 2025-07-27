from flask_restful import Resource

# from fairino import Robot

# A connection is established with the robot controller. A successful connection returns a robot object
# robot = Robot.RPC("192.168.58.2")


class FairinoControl(Resource):
    """
    API sử dụng để truyền action cũng như check connection đến Fairino Robot
    """

    def post(self, command):
        if command == "check-connection":
            return "check connection has run!"
        # elif command == "test":
        #     print("WaitAI start")
        #     error = robot.WaitAI(id=0, sign=0, value=50, maxtime=5000, opt=2)
        #     print("WaitAI return ", error)
        #     return "test command has run!"
        else:
            return "Command '" + command + "' not found!"
