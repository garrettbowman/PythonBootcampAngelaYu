from turtle import Turtle, Screen

PADDLE_SIZE = 5
STARTING_POSITIONS_RIGHT = [(330,40),(330,20),(330,0),(330,-20),(330,-40)]
STARTING_POSITIONS_LEFT = [(-330,40),(-330,20),(-330,0),(-330,-20),(-330,-40)]
MOVEMENT_SPEED = 40

class Paddle:

    def __init__(self, side):
        if side == "r":
            self.side = STARTING_POSITIONS_RIGHT
        else:
            self.side = STARTING_POSITIONS_LEFT
        self.segments = []
        self.create_paddle()
        self.head = self.segments[0]


    def create_paddle(self):
        for x in range(PADDLE_SIZE):
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.setheading(90)
            segment.shapesize(stretch_wid=.5, stretch_len=1)
            segment.speed("fastest")
            segment.goto(self.side[x][0], self.side[x][1])
            segment.penup()
            self.segments.append(segment)

    def move_up(self):
        for x in range(0,len(self.segments)):
            self.segments[x].setheading(90)
            self.segments[x].forward(MOVEMENT_SPEED)
    def move_down(self):
        for x in range(0,len(self.segments)):
            self.segments[x].setheading(270)
            self.segments[x].forward(MOVEMENT_SPEED)

    # def move(self):
    #     self.head.forward(MOVEMENT_SPEED)
    #     for segment in self.segments[1:]:
    #         self.segments[segment].goto(self.segments[segment-1].pos())
    #
    #     self.head_spot = self.segments[0].pos()

    def game_over(self):
        spot = self.segments[0].pos()
        spots = []
        # for _ in range(1,len(self.segments)):
        #     spots.append(self.segments[_].pos())
        #     if self.segments[_].distance(self.segments[0]) < 11:
        #         return True
        for _ in self.segments[1:]:
            if _.distance(self.segments[0]) < 11:
                return True
        if abs(spot[0]) > 280:
            return True
        elif abs(spot[1]) > 280:
            return True
        # elif self.segments[0].distance(spot)< 5:
        #     return True
        else:
            return Fals