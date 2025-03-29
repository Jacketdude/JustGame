from pyray import *

# Let's Create a Pong Game!

class MyGame:
    def __init__(self):
        self.WINWIDTH = 900
        self.WINHEIGHT = 600

        init_window(self.WINWIDTH, self.WINHEIGHT, "Hi :)")
        set_target_fps(60)

        self.ballx = self.WINWIDTH // 2
        self.bally = self.WINHEIGHT // 2
        self.ballrad = 15

        # Common Paddle Properties
        self.paddleSpeed = 10
        self.paddleWidth = 15
        self.paddleHeight = 90

        #Paddle 1
        self.paddle1x = 10
        self.paddle1y = self.WINHEIGHT // 2

        # Paddle 2
        self.paddle2x = self.WINWIDTH - 20
        self.paddle2y = self.WINHEIGHT // 2

    def Update(self):
        # Paddle1 Movement
        if is_key_down(KeyboardKey.KEY_W):
            self.paddle1y -= self.paddleSpeed
        
        if is_key_down(KeyboardKey.KEY_S):
            self.paddle1y += self.paddleSpeed

        if is_key_down(KeyboardKey.KEY_UP):
            self.paddle2y -= self.paddleSpeed

        if is_key_down(KeyboardKey.KEY_DOWN):
            self.paddle2y += self.paddleSpeed

        # Yeah, Clamping Rocks!
        self.paddle1y = int(clamp(float(self.paddle1y), 0, (self.WINHEIGHT - self.paddleHeight)))
        self.paddle2y = int(clamp(float(self.paddle2y), 0, (self.WINHEIGHT - self.paddleHeight)))


    def Draw(self):
        begin_drawing()
        
        clear_background(BLACK)
        draw_circle(self.ballx, self.bally, self.ballrad, WHITE)
        draw_rectangle(self.paddle1x, self.paddle1y, self.paddleWidth, self.paddleHeight, WHITE)
        draw_rectangle(self.paddle2x, self.paddle2y, self.paddleWidth, self.paddleHeight, WHITE)

        end_drawing()

    def Run(self):
        while not window_should_close():
            self.Update()
            self.Draw()
        close_window()

if __name__ == "__main__":
    app = MyGame()
    app.Run()
