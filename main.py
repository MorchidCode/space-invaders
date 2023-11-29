from turtle import *
import random

# Create the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

# Player setup
player = Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Player movement speed
player_speed = 15

# Move the player to the left
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

# Move the player to the right
def move_right():
    x = player.xcor()
    x += player_speed 
    if x > 280:
        x = 280
    player.setx(x)

# Bullet setup
bullet = Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# Bullet movement speed
bullet_speed = 20

# Bullet state
bullet_state = "ready"

# Function to fire the bullet
def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        # Move the bullet to the player's current position
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def move_bullet():
    global bullet_state
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

# Create enemies
number_of_enemies = 10 
enemies = []

# Enemy setup
for i in range(number_of_enemies):
    # Create the enemy
    enemy = Turtle()
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    # Position the enemy
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
    # Add the enemy to the list
    enemies.append(enemy)

enemy_speed = 2  # Speed at which the enemy moves

def move_enemies():
    global enemy_speed
    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Reverse direction and move down if at the edge
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change the enemy direction
            enemy_speed *= -1

def isCollision(t1, t2):
    distance = t1.distance(t2)
    if distance < 15:
        return True
    else:
        return False

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")

while True:
    screen.update()  # Update the screen
    move_bullet()  # Move the bullet
    move_enemies()

    # Check for bullet collision with the enemy
    for enemy in enemies:
        if isCollision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)  # Move the bullet out of the screen

            # Remove the enemy
            enemy.hideturtle()
            enemy.clear()  # Clear any traces of the enemy
            enemies.remove(enemy)
