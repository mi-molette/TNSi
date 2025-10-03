from PIL import Image, ImageDraw, ImageFont
import sys
import inspect

class PyxelArt :
    
    def __init__(self, w, h, s=20):
        self.w = w
        self.h = h
        self.s = s
        self.i = 1
        self.l = False
        #self.correctionDetaille = False # Mettre a True pour une correction détaillée (numéro de ligne du programme coloriant la case)
        self.lines = []
        #self.font = ImageFont.truetype("https://capytale2.ac-paris.fr/web/sites/default/files/2025/09-22/10-06-10/LiberationMono-Bold.ttf", self.s)
        #self.font = ImageFont.truetype("https://capytale2.ac-paris.fr/web/sites/default/files/2025/09-22/10-06-10/LiberationMono-Bold.ttf", int(self.s*0.75))
        self.output = Image.new('RGB', ((w+1)*(self.s+1), (h+1)*(self.s+1)), (255,255,255))
        self.draw = ImageDraw.Draw(self.output)
        for x in range(0,w+1) :
            self.draw.line([
                (x+1)*(self.s+1)-1,
                0,
                (x+1)*(self.s+1)-1,
                (h+1)*(self.s+1)
            ], fill=(0,0,0))
        for x in range(0,w) :
            self.draw.text(((x+2)*(self.s+1)-1-self.s/2,self.s/2), str(x), fill=(0, 0, 0), anchor="mm")
        for y in range(0,h+1) :
            self.draw.line([
                0,
                (y+1)*(self.s+1)-1,  
                (w+1)*(self.s+1),
                (y+1)*(self.s+1)-1
            ], fill=(0,0,0))
        for y in range(0,h) :
            self.draw.text((self.s/2,(y+2)*(self.s+1)-1-self.s/2), str(y), fill=(0, 0, 0), anchor="mm")
 
 
    # 16 basic colors (VGA palette)
    COLORS = {
        0: (0, 0, 0),         # black
        1: (128, 0, 0),       # maroon
        2: (0, 128, 0),       # green
        3: (128, 128, 0),     # olive
        4: (0, 0, 128),       # navy
        5: (128, 0, 128),     # purple
        6: (0, 128, 128),     # teal
        7: (192, 192, 192),   # silver
        8: (128, 128, 128),   # gray
        9: (255, 0, 0),       # red
        10: (0, 255, 0),      # lime
        11: (255, 255, 0),    # yellow
        12: (0, 0, 255),      # blue
        13: (255, 0, 255),    # fuchsia
        14: (0, 255, 255),    # aqua
        15: (255, 255, 255),  # white
        # Named aliases
        'black': (0, 0, 0),
        'maroon': (128, 0, 0),
        'green': (0, 128, 0),
        'olive': (128, 128, 0),
        'navy': (0, 0, 128),
        'purple': (128, 0, 128),
        'teal': (0, 128, 128),
        'silver': (192, 192, 192),
        'gray': (128, 128, 128),
        'red': (255, 0, 0),
        'lime': (0, 255, 0),
        'yellow': (255, 255, 0),
        'blue': (0, 0, 255),
        'fuchsia': (255, 0, 255),
        'aqua': (0, 255, 255),
        'white': (255, 255, 255),
    }

    def colorier(self, x, y, color=None):
        # Default color: gray
        rgb = (150, 150, 150)
        if color is not None:
            if isinstance(color, int):
                rgb = self.COLORS.get(color, rgb)
            elif isinstance(color, str):
                rgb = self.COLORS.get(color.lower(), rgb)
            elif isinstance(color, (tuple, list)) and len(color) == 3:
                rgb = tuple(color)
        self.draw.rectangle([
            (x+1)*(self.s+1),
            (y+1)*(self.s+1),
            (x+1)*(self.s+1)+self.s-1,
            (y+1)*(self.s+1)+self.s-1], fill=rgb)
        
    def show(self) :
        if __file__.split('\\')[0] in ('generer_moodle.py', 'generer_pronote.py') : return
        self.output.show()
        
         
    def reset(self):
        # Réinitialiser l'image avec une nouvelle grille vide
        self.output = Image.new('RGB', ((self.w+1)*(self.s+1), (self.h+1)*(self.s+1)), (255,255,255))
        self.draw = ImageDraw.Draw(self.output)
        # Redessiner la grille
        for x in range(0,self.w+1):
            self.draw.line([
                (x+1)*(self.s+1)-1,
                0,
                (x+1)*(self.s+1)-1,
                (self.h+1)*(self.s+1)
            ], fill=(0,0,0))
        for x in range(0,self.w):
            self.draw.text(((x+2)*(self.s+1)-1-self.s/2,self.s/2), str(x), fill=(0, 0, 0), anchor="mm")
        for y in range(0,self.h+1):
            self.draw.line([
                0,
                (y+1)*(self.s+1)-1,  
                (self.w+1)*(self.s+1),
                (y+1)*(self.s+1)-1
            ], fill=(0,0,0))
        for y in range(0,self.h):
            self.draw.text((self.s/2,(y+2)*(self.s+1)-1-self.s/2), str(y), fill=(0, 0, 0), anchor="mm")
    
    def afficher(self, name=None):
        self.show()
        # Réinitialiser après l'affichage
        self.reset()
        
pa = PyxelArt(9,9)

for f in [f for f in dir(PyxelArt) if not f.startswith('_')] :
    globals()[f] = getattr(pa, f)
