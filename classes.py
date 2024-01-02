class Ball:
    def __init__(self, skin ,radius, position, velocity, gravity):
        self._skin   = str(skin)
        self._radius = radius
        self._position = position
        self._velocity = velocity
        self._gravity  = gravity

    #access data
    def get_position(self):
        return self._position
    def get_velocity(self):
        return self._velocity

    #update position
    def update_position(self):
        self._velocity[0] += self._gravity[0]
        self._velocity[1] += self._gravity[1]
        self._position[0] += self._velocity[0]
        self._position[1] += self._velocity[1]



class Rect:
    def __init__(self, size, position, velocity):
        self._position = position
        self._velocity = velocity
    
class Circ:
    def __init__(self, radius, position, velocity):
        self._position = position
        self._velocity = velocity
    