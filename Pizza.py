from superwires import games, color
import random

SCORE = 0




   
##    pizza_image= games.load_image("images/pizza.png")
##    pizza = games.Sprite(image = pizza_image, x=SW/2, y=SH/2,
##                         dx =1, dy = 1)
##    games.screen.add(pizza)

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    """ A pan controlled by the mouse. """
    def update(self):
        """ Move to mouse coordinates """
        self.x = games.mouse.x
        #self.y = games.mouse.y
        self.check_collide()
    def check_collide(self):
        """ Check for collision with pizza. """
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()
            
    
class Pizza(games.Sprite):

    def update(self):
        global SCORE
        #bouncing 
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            #SCORE += 1

        #if self.bottom > games.screen.height or
        if self.top < 0:
            self.dy = -self.dy
            #SCORE += 1
        
##        if self.left > games.screen.width:
##            self.right = 0
##            SCORE +=1
##        if self.right<0:
##           self.left =  games.screen.width
##           SCORE +=1
##
##        if self.top > games.screen.height:
##            self.top = 0
##            SCORE +=1
##        if self.bottom < 0:
##            self.bottom = games.screen.height
##            SCORE +=1
##           
    def handle_collide(self):
        #self.x = random.randrange(games.screen.width)
        self.dy = -self.dy
            


class ScText(games.Text):
    def update(self):
        self.value = SCORE

def main():
     # loaded img
    bg_img = games.load_image("images/pizzeria.jpg", transparent = True)
    pizza_img = games.load_image("images/pizza.png")
    pan_img = games.load_image("images/mousepoint.png")

    #added img to bg
    games.screen.background = bg_img

    #create pizza obj
    pizza = Pizza(image = pizza_img, x=games.screen.width/2, y=games.screen.height/2,
                         dx =random.randint(-10,10), dy = random.randint(-10,10))
    pizza2 = Pizza(image = pizza_img, x=games.screen.width/2, y=games.screen.height/2,
                         dx =random.randint(-10,10), dy = random.randint(-10,10))
    pizza3 = Pizza(image = pizza_img, x=games.screen.width/2, y=games.screen.height/2,
                         dx =random.randint(-10,10), dy = random.randint(-10,10))
    pizza4 = Pizza(image = pizza_img, x=games.screen.width/2, y=games.screen.height/2,
                         dx =random.randint(-10,10), dy = random.randint(-10,10))

    #create pan obj
    pan = Pan(image = pan_img, x=games.mouse.x, y=games.mouse.y)
    
    
                    
                    
                    

    #create txt obj
    score = ScText(value = SCORE, size = 60,
                   is_collideable = False,
                   color = color.black,
                   x = 550,
                   y = 30)

    #draw objs to screen
    games.screen.add(pizza)
    games.screen.add(pizza2)
    games.screen.add(pizza3)
    games.screen.add(pizza4)
    games.screen.add(score)
    games.screen.add(pan)
    
    #sets visibility of mouse while on screen
    games.mouse.is_visible = False

    #locks mouse to screen if True
    games.screen.event_grab = False


    #start mainloop
    games.screen.mainloop()


    #score = games.Text(value = "welcome", size = 60, color = color.black, x = 550, y = 30)
    games.screen.add(score)

####    won_message = games.Message(value = "You lose!", color = color.blue, size = 100, x = games.screen.width/2, y = games.screen.height/2, lifetime = 250, after_death = games.screen.quit)
####    games.screen.add(won_message)

##game_over = games.Message(value = "Game Over",
##                          size = 100,
##                          color = color.blue,
##                          x = games.screen.width/2
##                          y = games.screen.height/2
##                          lifetime = 250,
##                          after_death = games.screen.quit)
##games.screen.add(game_over)

main()





##angle - Facing in degrees
##
##x - x-coordinate
##
##y - y-coordinate
##
##dx - x velocity
##
##dy - y velocity
##
##left - x-coordinate of left sprite edge
##
##right - x-coordinate of right sprite edge
##
##top - y-coordinate of top sprite edge
##
##bottom - y-coordinate of bottom sprite edge
##
##image - image object of sprite
##
##overlapping_sprites - List of other objects that overlap sprite
##
##is_collideable - Whether or not the sprite is collideable. True means sprite will register in collisions. False means sprite will not show up in collisions.

##Methods
##
##update() - Updates sprite. Automatically called every mainloop() cycle.
##
##destroy() - Removes sprite from the screen
