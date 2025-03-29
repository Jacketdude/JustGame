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

        self.paddle1x = 
        self.paddle1y = self.WINHEIGHT // 2

    def Update(self):
        pass

    def Draw(self):
        begin_drawing()

        draw_circle(self.ballx, self.bally, self.ballrad, WHITE)
        draw_rectangle()

        end_drawing()

    def Run(self):
        while not window_should_close():
            self.Update()
            self.Draw()
        close_window()

if __name__ == "__main__":
    app = MyGame()
    app.Run()