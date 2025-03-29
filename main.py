from pyray import *

class MyGame:
    def __init__(self):
        self.WINWIDTH = 900
        self.WINHEIGHT = 600

        init_window(self.WINWIDTH, self.WINHEIGHT, "Hi :)")
        set_target_fps(60)

        self.PlayerX = self.WINWIDTH // 2
        self.PlayerY = self.WINHEIGHT // 2
        self.playerSpeed = 20

    def Update(self):
        if (is_key_down(KeyboardKey.KEY_W)):
            self.PlayerY -= self.playerSpeed
        if (is_key_down(KeyboardKey.KEY_A)):
            self.PlayerX -= self.playerSpeed
        if (is_key_down(KeyboardKey.KEY_S)):
            self.PlayerY += self.playerSpeed
        if (is_key_down(KeyboardKey.KEY_D)):
            self.PlayerX += self.playerSpeed

    def Draw(self):
        draw_circle(self.PlayerX, self.PlayerY, 20, WHITE)

    def Run(self):
        while not window_should_close():
            self.Update()
            begin_drawing()
            clear_background(BLACK)
            self.Draw()
            end_drawing()
        close_window()

if __name__ == "__main__":
    app = MyGame()
    app.Run()