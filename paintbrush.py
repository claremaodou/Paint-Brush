# Paint Brush 
import pygame

# User-defined functions
def main():
   # initialize all pygame modules 
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Painting')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play()  
   # quit pygame and clean up the pygame window
   pygame.quit() 
   
# User-defined classes
class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      self.bg_color = pygame.Color('black')
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      
      # === game specific objects
      self.default_color = 'red'
      self.brush = Paintbrush(250, 200, 10, 10,self.default_color, [0,0], self.surface)

   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.
      while not self.close_clicked:  # until player clicks close box
         # play frame
         x = self.handle_events()
         self.draw()            
         if self.continue_game:
            self.update()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled
      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.KEYDOWN:
            x = self.handle_keydown(event)
         if event.type == pygame.KEYUP:
            self.handle_keyup(event)
     
   def handle_keyup(self, event):
      # if event key is not pressed then brush will not move:
       # - event is the pygame events
      if event.key == pygame.K_UP:
         self.brush.stopVertical()  
      if event.key == pygame.K_DOWN:
         self.brush.stopVertical() 
      if event.key == pygame.K_RIGHT:
         self.brush.stopHorizontal()
      if event.key == pygame.K_LEFT:
         self.brush.stopHorizontal()
         
   def handle_keydown(self, event):
      # if event key is pressed then brush will move
      # - self is the Game 
      # - event is the pygame events   
      if event.key == pygame.K_UP:
         self.brush.moveUp()
      if event.key == pygame.K_DOWN:
         self.brush.moveDown() 
      if event.key == pygame.K_RIGHT:
         self.brush.moveRight()
      if event.key == pygame.K_LEFT:
         self.brush.moveLeft()
      if event.key == pygame.K_r:
         self.brush.set_color('red')
      if event.key == pygame.K_g:
         self.brush.set_color('green')
      if event.key == pygame.K_b:
         self.brush.set_color('blue')
      if event.key == pygame.K_y:
         self.brush.set_color('yellow')
      if event.key == pygame.K_SPACE:
         self.brush.set_color('black')
         
   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      self.brush.draw()
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update   
      self.brush.move()

class Paintbrush:
   def __init__(self, x, y, width, height, color, velocity, surface):
      # - self is the Paintbrush class to initialize 
      # - x is the x-coor int
      # - y is the y-coor int
      # - width is the width int
      # - height is the height int
      # - color is the color string
      # - velocity is the speed list
      # - surface is the display window surface object
      self.rect = pygame.Rect(x, y, width, height) # "geometry" of the rectangle
      self.color = pygame.Color(color)
      self.velocity = velocity
      self.surface = surface
          
   def move(self): 
   # set the bounderies of the window
   # - self is the Game which moves the brush    
      self.rect.move_ip(self.velocity[1], self.velocity[0])
      if self.rect.top <= 0 or self.rect.bottom >= self.surface.get_height(): 
         self.velocity[0] = 0   
      if self.rect.left <= 0 or self.rect.right >= self.surface.get_width():
         self.velocity[1] = 0
      
   def moveUp(self):
   # - self is the brush which moves up
      self.velocity[0] = -5
       
   def moveDown(self):
   # - self is the brush which moves Rect down
      self.velocity[0] = 5
      
   def stopVertical(self):
   # - self is the brush to stop Rect vertically
      self.velocity[0] = 0
      
   def moveRight(self):
   # - self is the brush to moves Rect right
      self.velocity[1] = 5
      
   def moveLeft(self):
   # - self is the brush which moves Rect left
      self.velocity[1] = -5
   
   def stopHorizontal(self):
   # - self is the brush which stops Rect horizontally
      self.velocity[1] = 0
   
   def draw(self):
   # - self is the brush which draws the Rect
      pygame.draw.rect(self.surface, self.color, self.rect)
   
   def set_color(self, color):
      # Changes the color of the dot
      # - self is the brush
      # - color is a string object representing a color name
      self.color = pygame.Color(color)   
      
main()
