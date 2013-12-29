from twisted.internet import task

import matrix
import message


class Game(object):
    """
    Implements the server for the car race
    """

    def __init__(self, server):
        self.server = server
        self.matrix = matrix.Matrix()
        self.lives = [3, 3, 3, 3]
        self.looper = task.LoopingCall(self.loop)
        self.player_id = 0
        self.started = False

    def start(self):
        assert not self.started
        self.started = True
        self.looper.start(1, now=False)
        msg = message.Message('update', {'matrix': self.matrix.matrix})
        self.server.broadcast(str(msg))

    def add_player(self):
        id = self.player_id
        self.player_id += 1
        print 'add_player:', id
        return id

    def remove_player(self, id):
        print 'remove_player:', id
        pass

    def update_player(self, info):
        print 'update_player:', info

    def loop(self):
        print 'loop'
        # Send updates to the clients
        # XXX process game logic here (self.do)
        self.matrix.matrix.pop()
        self.matrix.matrix.insert(0, self.get_next())
        msg = message.Message('update', {'next': self.matrix.matrix[0]})
        self.server.broadcast(str(msg))

    def get_next(self):
        """
        Returns the next row
        """
        return [1, 2, 3, 4]

    def do(self, car1_action, car2_action, car3_action, car4_action):
        """
        Gets action for each car
        Returns the new position of each car
        Available actions are:
        - Move forward
        - Move right
        - Move left
        - Jump
        - Pick (star)
        """
        pass

    def _pick(self, car_num):
        """
        Increase life for a car if there is a star there
        """
        x, y = get_location(car_num)
        if get_obstacle(x, y) == ENUMS.STAR:
            self.lives[car_num-1] = self.lives[car_num-1] + 1

    def _get_obstacle(self, x, y):
        """
        Return the obstacle in location x, y
        """
        pass
