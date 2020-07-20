import tkinter as tk
import random as rnd
from PIL import ImageTk, Image
from fractal import Fractal

####################### Window stuff ###################
def redraw(xOffset,yOffset,zoom):
    newImg = ImageTk.PhotoImage(fractal.genFractImg());
    pic.configure(image = newImg);
    pic.image = newImg;

# create window for image
windw = tk.Tk();
#windw.geometry("400x300");
#fractal = Fractal(400, 300, 100, 2);
windw.geometry("400x300");
fractal = Fractal(400, 300, 100, 2);

#separate window into image and controls frames
fract = tk.Frame(windw);
fract.pack(side = "top");

cont = tk.Frame(windw);
cont.pack(side = "bottom");

# place image in window
img = ImageTk.PhotoImage(fractal.returnImg());
pic = tk.Label(windw, image = img);
pic.pack(side = "left", fill = "both", expand = "yes");

#Controls
cLabel = tk.Label(cont, text="c = " + str(fractal.c.real) + "i" + str(fractal.c.imag));
cLabel.pack();
ranFract = tk.Button(cont, text = "random fractal", command = lambda: redraw(0, 0, 1));
ranFract.pack();

# draw stuff
windw.mainloop();
