if not (self._velocity[0] == 0  or self._velocity[1] ==0): #quick division 0 fix
                self._position[0] += 5 *(self._velocity[0]/abs(self._velocity[0]))  #bugfix to make some space between collision
                self._position[1] += 5 *(self._velocity[1]/abs(self._velocity[1]))  #bugfix to make some space between collision
            