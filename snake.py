from turtle import Turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    segments = []

    def __init__(self):

        for position in starting_positions:
            self.new_segment = Turtle("square")
            self.new_segment.penup()
            self.new_segment.color("white")
            self.new_segment.goto(position)
            self.segments.append(self.new_segment)

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)
