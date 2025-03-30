from pyray import *

# Let's Create a Pong Game!

class MyGame:
    def __init__(self):
        self.WINWIDTH = 900
        self.WINHEIGHT = 600

        init_window(self.WINWIDTH, self.WINHEIGHT, "The game that's totally not pong 🤔")
        set_target_fps(60)

        # Ball Properties
        self.ballx = self.WINWIDTH // 2
        self.bally = self.WINHEIGHT // 2
        self.ballrad = 15
        self.ballSpeed = 4
        self.ballvx = self.ballSpeed
        self.ballvy = self.ballSpeed

        # Common Paddle Properties
        self.paddleSpeed = 10
        self.paddleWidth = 15
        self.paddleHeight = 90

        #Paddle 1
        self.paddle1x = 10
        self.paddle1y = self.WINHEIGHT // 2

        # Paddle 2
        self.paddle2x = (self.WINWIDTH - self.paddleWidth) - 10
        self.paddle2y = self.WINHEIGHT // 2

        # Scoring Mechanism
        self.scorep1 = 0
        self.scorep2 = 0

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
        self.paddle1y = int(clamp(self.paddle1y, 0, self.WINHEIGHT - self.paddleHeight))
        self.paddle2y = int(clamp(self.paddle2y, 0, self.WINHEIGHT - self.paddleHeight))
        self.ballx = int(clamp(self.ballx, self.ballrad, self.WINWIDTH - self.ballrad))
        self.bally = int(clamp(self.bally, self.ballrad, self.WINHEIGHT - self.ballrad))

        self.ballx += self.ballvx
        self.bally += self.ballvy
        # If you have no friends
        self.paddle2y = self.bally - (self.paddleHeight // 2)

        #Testing 
        if self.bally - self.ballrad <= 0 or self.bally + self.ballrad >= self.WINHEIGHT:
            self.ballvy = -self.ballvy

        if self.ballx - self.ballrad <= self.paddleWidth and self.paddle1y < self.bally < self.paddle1y + self.paddleHeight:
            self.ballvx = -self.ballvx

        if self.ballx + self.ballrad >= self.WINWIDTH - self.paddleWidth and self.paddle2y < self.bally < self.paddle2y + self.paddleHeight:
            self.ballvx = -self.ballvx

    def Draw(self):
        begin_drawing()
        

        clear_background(BLACK)

        # Ball
        draw_circle(self.ballx, self.bally, self.ballrad, WHITE)

        # Paddles
        draw_rectangle(self.paddle1x, self.paddle1y, self.paddleWidth, self.paddleHeight, WHITE)
        draw_rectangle(self.paddle2x, self.paddle2y, self.paddleWidth, self.paddleHeight, WHITE)

        # Scoring
        draw_text(str(self.scorep1), (self.WINWIDTH // 4), 10, 50, BLUE)
        draw_text(str(self.scorep2), 3 * (self.WINWIDTH // 4), 10, 50, RED)


        end_drawing()

    def Run(self):
        while not window_should_close():
            self.Update()
            self.Draw()
        close_window()

if __name__ == "__main__":
    app = MyGame()
    app.Run()
