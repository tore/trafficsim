class TrafficLight:
    def __init__(self, greenSpeed):
        self.state = 0
        self.greenSpeed = greenSpeed
        
    def tick(self):
        self.state += 1
        
    def getSpeed(self):
        if (self.state % 5 == 0):
            return self.greenSpeed
        else:
            return 0
            #return self.greenSpeed