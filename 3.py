import turtle
import time
import random

delay = 0.12
score = 0
high_score = 0
neon_colors = ["#FF007F", "#00F0FF", "#39FF14", "#FFEA00", "#B026FF", "#FF5E00"]

screen = turtle.Screen()
screen.title("Neon Speed Snake")
screen.bgcolor("#121215")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("turtle")
head.color("#FFFFFF")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(random.choice(neon_colors))
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#E0E0E0")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 22, "bold"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

while True:
    screen.update()

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        delay = 0.12
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 22, "bold"))

    if head.distance(food) < 20:
        x = random.randint(-270, 270) // 20 * 20
        y = random.randint(-270, 250) // 20 * 20
        food.goto(x, y)
        food.color(random.choice(neon_colors))

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color(random.choice(neon_colors))
        new_segment.penup()
        segments.append(new_segment)

        delay = max(0.03, delay - 0.004)
        score += 10
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 22, "bold"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            
            score = 0
            delay = 0.12
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 22, "bold"))

    time.sleep(delay)

screen.mainloop()