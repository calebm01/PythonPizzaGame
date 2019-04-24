#Epic Pizza Game
#Created by Caleb Mouritsen
# 4/18/19


#imports
from superwires import games, color
import random





#screen creation
games.init(screen_width = 640, screen_height = 480, fps = 60)

Lives = 3




#classes
class Pizza(games.Sprite):
    #load the img
    image = games.load_image("images/pizza.png")
    speed = random.randrange(1,10)

    def __init__(self, x, y = 64 ):
        super(Pizza,self).__init__(image = Pizza.image, x = x, y = y, dy = Pizza.speed)
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        
    def update(self):
        if self.top > games.screen.height:
            self.destroy()
        if Lives = 0:
            self.end_game()
    def handle_caught(self):
        self.destroy()
    def end_game(self):
        end_message = games.Message(value = "Game Over",
                                    size = 120,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5*games.screen.fps,
                                    after_death =  games.screen.quit)
        games.screen.add(end_message)

    
class Pan(games.Sprite):
    image = games.load_image("images/mousepoint.png")
    def __init__(self):
        super(Pan, self).__init__(image = Pan.image, x = games.mouse.x, bottom = games.screen.height)
        
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0

        if self. right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()
    def check_catch(self):
        for pizza in self.overlapping_sprites:
            pizza.handle_caught()
            self.score.value += 10
            self.score.right = games.screen.width - 10
    
class Chef(games.Sprite):
    image = games.load_image("images/chef.png")
    def __init__(self, y = 55, speed = 5, odds_change = 100):
        super(Chef,self).__init__(image = Chef.image,x = games.screen.width / 2, y = y, dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0
    def update(self):
        if self.left < 0 or self. right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()

    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            self.time_til_drop = random.randrange(10, 200)
            

class ScText(games.Sprite):
    pass










#main
def main():


    #load imgs
    wall_image = games.load_image("images/pizzeria.jpg" , transparent = True)


    #create game objects
    the_pan = Pan()
    the_chef = Chef()
    the_pizza = Pizza(200)


    #draw objects to screen
    games.screen.background = wall_image
    games.screen.add(the_pan)
    games.screen.add(the_chef)
    games.screen.add(the_pizza)


    #mouse setup
    games.mouse.is_visible = False
    games.screen.event_grab = True



    #start game loop
    games.screen.mainloop()




#startup
main()
