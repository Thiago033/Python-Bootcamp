from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

#Directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)
    
    
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
            
        self.head.forward(MOVE_DISTANCE)
        
        
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
        
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
        
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)