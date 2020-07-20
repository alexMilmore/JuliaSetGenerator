import random as rnd
from PIL import ImageTk, Image
import numpy as np

# The speed of this could be improved by moving the fractal generation and the
# colouring into the same loop, however this would prevent easy changing of colours
# without changing the fractal. It would be better to use CUDA to run this on the gpu
# instead of moving both processes into one loop.
class Fractal:
    def __init__(self, xPixels, yPixels, iterationLimit, cutoff):
        self.xPixels = xPixels;
        self.yPixels = yPixels;
        self.iterationLimit = iterationLimit;
        self.cutoff = cutoff;

        #-0.8696+0.26i
        # -0.79,0.15
        self.c = complex(-0.7269,-0.1889);
        self.mandlebrot = False;
        self.juliaSet = self.juliaSetGen(self.c)
        self.image = self.genImg(self.juliaSet);

    def returnImg(self):
        # Uncomment if you want to save the image
        #self.image.save("julia.png");
        #print("save")
        return self.image;

    def genFractImg(self):
        self.c = self.cGen();
        self.juliaSet = self.juliaSetGen(self.c);
        self.im = self.genImg(self.juliaSet);
        return self.im;

    def juliaSetGen(self, c):
        self.c = c;
        # We want the origin at the centre of the screen, so we offset the origin
        xOffset = int(self.xPixels/2);
        yOffset = int(self.yPixels/2);
        data = np.zeros((self.xPixels, self.yPixels), dtype=np.int);
        for x in range(0, self.xPixels):
            for y in range(0, self.yPixels):
                # scale by xPixels to keep y scaling consistent with x (we dont want to warp the image)
                xCoord = (x-xOffset)/(self.xPixels/4);
                yCoord = (y-yOffset)/(self.xPixels/4);
                data[x,y] = self.valAtPoint(xCoord,yCoord,c);
        return data;

    def genRandJuliaSet(self):
        self.c = self.cGen();
        return self.juliaSetGen(self.c);

    # Calculates the value of a julia set at a point
    def valAtPoint(self, x, y, c):
        z = complex(x,y);
        for iteration in range(0, self.iterationLimit):
            # if julia;          z_n = z^2 + c
            # if mandlebrot;     z_n = z^2 + c
            z = self.iterateZ(z, c);
            value = int(iteration*255/self.iterationLimit);
            # no longer bounded
            if abs(z) > self.cutoff:
                return value;
        return value;

    def iterateZ(self, z, c):
        if self.mandlebrot == True:
            return z*z + z;
        return z*z + c

    # Generates random complex numbers
    def cGen(self):
        re = rnd.randint(-100,100)/100;
        im = rnd.randint(-100,100)/100;
        c = complex(re,im);
        return c;

    def genImg(self, juliaSet):
        im = Image.new("RGB", (self.xPixels, self.yPixels));
        pix = im.load();
        for x in range(0, self.xPixels):
            for y in range(0, self.yPixels):
                pix[x,y] = self.colourGen(juliaSet[x,y], juliaSet.max());
        return im;

    # converts a number from 0-255 into more interesting colours
    def colourGen(self, n, scale):
        val = int(255*n/scale);

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
