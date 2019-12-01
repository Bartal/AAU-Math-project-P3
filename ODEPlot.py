import numpy as np
from matplotlib import pyplot as plt, ticker
from scipy import integrate


class ODEPlot:
    def __init__(self, function_1, function_2, xAsix, yAxis, tRange=(-20, 20)):
        self.function_1 = function_1
        self.function_2 = function_2
        self.tStart, self.tEnd = tRange
        self.function = lambda x, y, t=0: [self.function_1(x, y), self.function_2(x, y)]
        self.xStart, self.xEnd = xAsix
        self.yStart, self.yEnd = yAxis
        self.points = []
        self.startConditions = []
        self.artist = []

    def addPoint(self, x, y, color):
        self.points.append((x, y, color))

    def addInitalStartConditons(self, x, y, color):
        self.startConditions.append((x, y, color))

    def addCircle(self, x, y, radius, color='black', lineType='--'):
        self.artist.append(plt.Circle((x, y), radius, color=color, fill=False, linestyle=lineType))

    def save(self, filename):
        # plt.style.use('ggplot')
        np.seterr(divide='ignore', invalid='ignore')

        x = np.linspace(self.xStart, self.xEnd, 30)
        y = np.linspace(self.yStart, self.yEnd, 30)
        X1, Y1 = np.meshgrid(x, y)
        dx1, dx2 = self.function(X1, Y1)

        M = (np.hypot(dx1, dx2))
        M[M == 0] = 1.
        dx1 /= M
        dx2 /= M

        plt.figure()
        plt.quiver(x, y, dx1, dx2, M)

        for point in self.points:
            x, y, color = point
            plt.plot(x, y, 'o', color=color)

        N = 500
        t = np.linspace(self.tStart, self.tEnd, N)
        for start in self.startConditions:
            x, y, color = start

            tNegative = t[t < 0]
            tPositve = t[t >= 0]

            def fun(p, t):
                return self.function(p[0], p[1], t)

            if len(tNegative) > 0:
                output = integrate.odeint(fun, [x, y], tNegative)
                plt.plot(output[:, 0], output[:, 1], color=color)
            if len(tPositve) > 0:
                output = integrate.odeint(fun, [x, y], tPositve)
                plt.plot(output[:, 0], output[:, 1], color=color)

        ax = plt.gca()
        for circle in self.artist:
            ax.add_artist(circle)

        plt.grid(False)
        plt.xlim(self.xStart, self.xEnd)
        plt.ylim(self.yStart, self.yEnd)
        # TODO move to own function

        ax.grid(True)
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.tick_params(axis='both', which='major', labelsize=8)
        ax.tick_params(axis='both', which='minor', labelsize=6)
        func = lambda x, pos: "" if np.isclose(x, 0) else x
        plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(func))
        plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(func))

        plt.savefig(filename, dpi=400)


def run():
    ode = ODEPlot(lambda x, y: -x + y, lambda x, y: -y, (-10, 10), (-10, 10))
    ode.addPoint(0, 0, 'black')
    ode.addInitalStartConditons(2, 2, 'black')
    ode.save('test.png')


run()
