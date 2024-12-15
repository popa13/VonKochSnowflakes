from numpy import *
from matplotlib import pyplot as plt

from numpy import *
from matplotlib import pyplot as plt


class KochCurve:

    def __init__(self, l, n):
        # Set the lenght of the isoseles triangle
        if l >= 0.25 and l <= 0.5:
            self.l = l
        else:
            self.l = 0.3333
            print("""The length is not between 0.25 and 0.5. The length has been set to the default value
                  of 0.3333 giving the classical Von Koch Curve.""")
        # Set the number of iterations
        self.n = int(n)
        # Set the parameters that depends on l
        # a: The amount removed at the base
        # b: the length of the height of the isosceles triangle
        # theta: The size of the two congruent angle in the isosceles triangle
        # c: cos (theta)
        # s: sin (theta)
        # yOffset: the height where the curve is drawn in the screen
        self.a = 1 / 2 - self.l
        if self.l >= 0.25:
            self.b = sqrt(self.l ** 2 - self.a ** 2)
        else:
            self.b = 0
        theta = arctan(self.b / self.a)
        self.c = cos(theta)
        self.s = sin(theta)
        self.rot = self.c + 1j * self.s
        self.rotAnti = self.c - 1j * self.s
        self.yOffset = 0.25
        # list of points to draw the KochCurve
        self.listOfPoints = []
        # initialize the curve
        self.iteration()

    # These are the four similitudes applied to the initial point (0,0)
    def f1(self, z):
        return self.l * z

    def f2(self, z):
        return self.l * self.rot * z + self.l

    def f3(self, z):
        return self.l * self.rotAnti * z + (1/2 + 1j * self.b)

    def f4(self, z):
        return self.l * z + (1 - self.l)

    def iteration(self):
        listPoints = [0]
        for j in linspace(1, self.n, self.n):
            tempListPoints = listPoints
            listPoints = []
            for p in tempListPoints:
                listPoints.append(self.f1(p))
            for p in tempListPoints:
                listPoints.append(self.f2(p))
            for p in tempListPoints:
                listPoints.append(self.f3(p))
            for p in tempListPoints:
                listPoints.append(self.f4(p))
        listPoints.append(1)
        self.listOfPoints = listPoints

    def __str__(self):
        if self.listOfPoints == []:
            toPrint = "First run iteration to set the list of points."
        else:
            toPrint = ""
            for p in self.listOfPoints:
                toPrint += str(p) + "\n"
        return toPrint

    def plotCurve(self):
        # Drawing the first horizontal part
        if self.listOfPoints == []:
            print("First run iteration to set the list of points.")
        else:
            xCoord, yCoord = [], []
            for p in self.listOfPoints:
                xCoord.append(p.real)
                yCoord.append(p.imag + self.yOffset)
            if self.n > 4:
                lineWidth = 1 / pow(2, self.n - 5)
                plt.plot(xCoord, yCoord, color='blue', linewidth=lineWidth)
            else:
                plt.plot(xCoord, yCoord, color='blue')
            plt.xlim(0, 1)
            plt.ylim(0, 1)
            plt.axis('off')
            plt.savefig('Koch-curve' + '.png', dpi=400, bbox_inches='tight')
            plt.close()

    def plotSnowFlake(self):
        #################################
        # Drawing the snowflake corresponding to the Koch Curve
        ######################################

        # Generation of the points for the
        # flipped and rotated of -60 version
        kochCurveFlipped = []
        c60 = cos(-pi / 3)
        s60 = sin(-pi / 3)
        rot60 = c60 + s60 * 1j
        for z in self.listOfPoints:
            kochCurveFlipped.append(z.conjugate())
        kochCurveFlippedAndRotated = []
        for z in kochCurveFlipped:
            newZ = rot60 * z
            kochCurveFlippedAndRotated.append(newZ)
        # Generate the list of points for the
        # rotated -120 and translate version
        kochCurveTranslatedAndRotated = []
        c120 = cos(-2 * pi / 3)
        s120 = sin(-2 * pi / 3)
        rot120 = c120 + 1j * s120
        for z in self.listOfPoints:
            newZ = rot120 * z + 1
            kochCurveTranslatedAndRotated.append(newZ)

        # Drawing the flipped and -60 rotated version
        xCoord, yCoord = [], []
        for z in kochCurveFlippedAndRotated:
            xCoord.append(z.real)
            yCoord.append(z.imag)
        if self.n > 4:
            lineWidth = 1 / pow(2, self.n - 5)
            plt.plot(xCoord, yCoord, color='blue', linewidth=lineWidth)
        else:
            plt.plot(xCoord, yCoord, color='blue')

        # Drawing the koch curve
        xCoord, yCoord = [], []
        for p in self.listOfPoints:
            xCoord.append(p.real)
            yCoord.append(p.imag)
        if self.n > 4:
            lineWidth = 1 / pow(2, self.n - 5)
            plt.plot(xCoord, yCoord, color='blue', linewidth=lineWidth)
        else:
            plt.plot(xCoord, yCoord, color='blue')

        # Drawing the translated and rotated -120 part
        xCoord = []
        yCoord = []
        for z in kochCurveTranslatedAndRotated:
            xCoord.append(z.real)
            yCoord.append(z.imag)
        if self.n > 4:
            lineWidth = 1 / pow(2, self.n - 5)
            plt.plot(xCoord, yCoord, color='blue', linewidth=lineWidth)
        else:
            plt.plot(xCoord, yCoord, color='blue')

        # plotting the snowflake
        plt.xlim(-0.355, 1.35)
        plt.ylim(-0.95, 0.555)
        plt.axis('off')
        plt.savefig('Koch-snowflake' + '.png', dpi=400, bbox_inches='tight')
        plt.close()