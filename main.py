from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import vlc


screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Tolstoi The Snake")
screen.tracer(0)

snake = Snake()
scoreboard = Scoreboard()
food = Food()

screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.b_left, key="Left")
screen.onkey(fun=snake.b_right, key="Right")

playlist = ["/Users/achimsondermann/Music/Splice/sounds/packs/"
            "Chiptune/""SM_White_Label_-_Chiptune_-_Wav/drum_loops/ct_drm128_ascension_top.mp3"]

player = vlc.MediaPlayer(playlist[0])
player.audio_set_volume(70)
game_on = True
while game_on:
    # player.play()
    screen.update()
    time.sleep(0.1)
    snake.move()
    # snake eats food
    if snake.head.distance(food) < 15:
        player = vlc.MediaPlayer("/Users/achimsondermann/Music/Splice/sounds/packs/Chip Drums/"
                                 "Chip_Drums/ATARI_2600/BULLYFINGER_chiptune_drum_one_shot_atari_2600_11.wav")
        scoreboard.get_score()
        food.refresh()
        snake.extend()
    # snake hits border
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        # player.stop()
        scoreboard.reset_score()
        snake.reset_snake()
        player = vlc.MediaPlayer("/Users/achimsondermann/Music/Splice/sounds/packs/Chiptune/"
                                 "SM_White_Label_-_Chiptune_-_Wav/fx/fallers/ct_fx_eraser.wav")
        #  player.play()
    # snake collides with itself
    for collide in snake.segments[1:]:
        if snake.head.distance(collide) < 15:
            # player.stop()
            scoreboard.reset_score()
            snake.reset_snake()
            # player = vlc.MediaPlayer("/Users/achimsondermann/Music/Splice/sounds/packs/Chiptune/"
            #                          "SM_White_Label_-_Chiptune_-_Wav/fx/fallers/ct_fx_eraser.wav")
            # player.play()

screen.exitonclick()
