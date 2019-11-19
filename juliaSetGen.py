import tkinter as tk
import random as rnd
from PIL import ImageTk, Image

size = 800;

# fractal function
#   num = number of iterations
num = 100;
cutoff = 2;
c = complex(-0.79,0.15);
random = True;
mandlebrot = False;

# Generates random complex numbers
def cGen():
    re = rnd.randint(-100,100)/100;
    im = rnd.randint(-100,100)/100;
    c = complex(re,im);
    return c

# converts a number from 0-255 into more interesting colours
def colourGen(n):
    if n < 85:
        val = n*3;
        colour = (val,0,0);
    elif n > 170:
        val = (n-170)*3;
        colour = (0,255-val,val);
    else:
        val = (n-170)*3;
        colour = (255-val,val,0);
    return colour

# Calculates the value of a julia set at a point
def fractal(x,y,c):
    z = complex(x,y);
    if mandlebrot == True:
        c = z;
    for iteration in range(num):
        z = z*z + c;
        colour = colourGen(int(iteration*255/num));
        if abs(z) > cutoff:
            return colour
    return colour;

#create image
def imgGen(size,xOffset,yOffset,zoom,c):
    imSize = size;
    xOffset = xOffset*size/4 + int(size/2);
    yOffset = yOffset*size/4 + int(size/2);
    scale = size/4*zoom;
    im = Image.new("RGB", (imSize,imSize));
    pix = im.load();
    for x in range(imSize):
        for y in range(imSize):
            xCoord = (x-xOffset)/scale;
            yCoord = (y-yOffset)/scale;
            pix[x,y] = fractal(xCoord,yCoord,c);

    im.save("test.png","PNG");

imgGen(size,0,0,1,c);

# create window for image
windw = tk.Tk();
windw.geometry("800x800");

#convert image for tkinter
path = "test.png";
img = ImageTk.PhotoImage(Image.open(path));

#separate window into image and controls frames
fract = tk.Frame(windw);
fract.pack(side = "left");

cont = tk.Frame(windw);
cont.pack(side = "right");

# place image in window
pic = tk.Label(windw, image = img);
pic.pack(side = "left", fill = "both", expand = "yes");

def redraw(size,xOffset,yOffset,zoom,c):
    imgGen(size,xOffset,yOffset,zoom,c);

    path = "test.png";
    newImg = ImageTk.PhotoImage(Image.open(path));
    pic.configure(image = newImg);
    pic.image = newImg;

# controls has 3 sliders
sZoom = tk.Scale(cont, from_ = 1, to = 10, label = "Zoom");
sZoom.pack();
sx = tk.Scale(cont, from_ = -5, to = 5, label = "x origin");
sx.pack();
sy = tk.Scale(cont, from_ = -5, to = 5, label = "y origin");
sy.pack();
# and 2 buttons
genB = tk.Button(cont, text = "scale fractal", command = lambda: redraw(size,sx.get(),sy.get(),sZoom.get(),c));
genB.pack();
ranB = tk.Button(cont, text = "random fractal", command = lambda: redraw(size,sx.get(),sy.get(),sZoom.get(),cGen()));
ranB.pack();

# draw stuff
windw.mainloop();
