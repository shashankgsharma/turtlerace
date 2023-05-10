import random
import turtle

print("Welcome to the Turtle Race!".upper())
width = int(input("Enter Screen Width: "))
height = int(input("Enter Screen Height: "))
print("Look for the 'Turtle Graphics Screen' on the pop-up window to enjoy the race!")

screen = turtle.Screen()


def race(screen_width, screen_height):

    screen.setup(width=screen_width, height=screen_height)

    turtles = {}
    colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    random.shuffle(colors)
    d = 0
    race_on = False

    for i in range(7):
        color = colors[i]
        turtles[color] = turtle.Turtle(shape="turtle")
        racer = turtles[color]
        racer.fillcolor(color)
        racer.penup()
        racer.goto(x=round(-screen_width / 2) + 20, y=round(-screen_height / 2) + 50 + d)
        d += round((screen_height - 2 * 20) / 7)

    guess = turtle.textinput(title="Bet on Turtle", prompt=f"Guess which turtle{colors} is gonna win the race: ")
    if guess is None:
        print("GOODBYE!")
        exit()
    else:
        guess = guess.lower()

    if guess:
        race_on = True

    while race_on:
        for color in turtles:
            racer = turtles[color]
            racer.speed(random.random())
            racer.forward(random.randint(1, 10))
            if racer.xcor() >= round(screen_width / 2) - 30:
                winner = color
                race_on = False

    if guess == winner:
        print(f"You were right, {winner} turtle won the race.\nAnd You won the bet!")
    else:
        print(f"You were wrong, {winner} turtle won the race.\nAnd You lost the bet.")


race(screen_width=width, screen_height=height)

screen.exitonclick()
