import pygame
import pkg_resources


class Text(pygame.sprite.Sprite):


    def __init__(self, sprite_or_stage, text, x=0, y=0, color=(255,255,255), fontsize=20):
        super().__init__()
        
        self.sprite_or_stage = sprite_or_stage
        # Visible sprites go into this group
        self.sprite_or_stage.stage.text_group.add(self)
        self._text = text
        self._color = color
        self._fontsize=fontsize
        self._font=pygame.font.Font(pkg_resources.resource_filename("pystage", "fonts/roboto-bold.ttf"), fontsize)
        self._defaultpos=(x,y)
        # Pygame coordinates, upper left corner
        self.image = None
        self.rect = None

        self.update_image()


    def update(self):
        pass #Fixme : delethe func ?


    def update_image(self):
        pos = self.rect.topleft if self.rect else self._defaultpos
        self.image = self._font.render(self._text, True, self._color)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


    def set_position(self, x,y):
        if not self.rect:
            self._defaultpos=(x,y)
            return
        self.rect.x = x + self.sprite_or_stage.stage.center_x
        self.rect.y = -y + self.sprite_or_stage.stage.center_y

    def set_text(self, text):
        if text != self._text:
            self._text=text
            self.update_image()

    def set_size(self, fontsize):
        if self._fontsize == fontsize: return 
        self._fontsize=fontsize
        self._font=pygame.font.Font(pkg_resources.resource_filename("pystage", "fonts/roboto-bold.ttf"), fontsize)
        self.update_image()

    def set_color(self, color):
        if self._color == color: return 
        self._color=color
        self.update_image()

        

    def show(self):
        self.sprite_or_stage.stage.text_group.add(self)
        self.update_image()


    def hide(self):
        self.sprite_or_stage.stage.text_group.remove(self)

    
    def remove(self):
        self.kill()
