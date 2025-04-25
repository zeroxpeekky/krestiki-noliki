from pygame import *
font.init()


window = display.set_mode((540,810))
display.set_caption('krestiki noliki')
zadniyfon = transform.scale(image.load("background.jpg"),(540,810))

clock = time.Clock()



class Wall(sprite.Sprite):
    def __init__(self, color_1,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill(color_1)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image,):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(100, 100))
class heatbox(sprite.Sprite):
    def __init__(self,heatbox_image,heatbox_x,heatbox_y):
        super().__init__()
        self.image = transform.scale(image.load(heatbox_image),(100, 100))
        self.rect= self.image.get_rect()
        self.rect.x = heatbox_x
        self.rect.y = heatbox_y
    def draw_heatbox(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



















class Player(GameSprite):
    def update(self):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            for  in :
                if card.rect.collidepoint(x,y):
                    
player = Player('krestik.png', 5 , 400, 4)


h1 = heatbox( 'heatbox.png', 270 , 405)
h2 = heatbox( 'heatbox.png', 200, 405)
h3 = heatbox( 'heatbox.png', 350 , 405) 
h4 = heatbox( 'heatbox.png', 270, 325)
h5 = heatbox( 'heatbox.png', 200, 325)
h6 = heatbox( 'heatbox.png', 350, 325)
h7 = heatbox( 'heatbox.png', 270, 485) 
h8 = heatbox( 'heatbox.png', 200, 485) 
h9 = heatbox( 'heatbox.png', 350, 485) 
heatboxes = [h1,h2,h3,h4,h5,h6,h7,h8,h9]



finish = False
game = True
while game == True:
    window.blit(zadniyfon,(0,0))
    
    
   
    for e in event.get():
        if e.type == QUIT:
            game = False    
    if finish != True:
        window.blit(zadniyfon,(0,0))
        for h in heatboxes:
            h.draw_heatbox()
    display.update()
    clock.tick(60)