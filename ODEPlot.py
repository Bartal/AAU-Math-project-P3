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

    def addPoint(self, x, y, color='cyan', label=None):
        self.points.append((x, y, color, label))

    def addInitalStartConditons(self, x, y, color, customTrange=None, legend=False):
        self.startConditions.append((x, y, color, customTrange, legend))

    def addCircle(self, x, y, radius, color='black', lineType='--', label=None):
        self.artist.append(plt.Circle((x, y), radius, color=color, fill=False, linestyle=lineType, label=label))

    def save(self, filename, numberOfArrows=(15,15)):
        # plt.style.use('ggplot')
        np.seterr(divide='ignore', invalid='ignore')

        x = np.linspace(self.xStart, self.xEnd, numberOfArrows[0])
        y = np.linspace(self.yStart, self.yEnd, numberOfArrows[1])
        X1, Y1 = np.meshgrid(x, y)
        dx1, dx2 = self.function(X1, Y1)

        M = (np.hypot(dx1, dx2))
        M[M == 0] = 1.
        dx1 /= M
        dx2 /= M

        plt.figure()
        plt.quiver(x, y, dx1, dx2, color='red', scale_units='xy', pivot='mid')

        for start in self.startConditions:
            x, y, color, customTrange, legend = start

            N = 500
            if customTrange is None:
                t = np.linspace(self.tStart, self.tEnd, N)
            else:
                t = np.linspace(customTrange[0], customTrange[1], N)
            tNegative = np.flip(t[t < 0])
            tPositve = t[t >= 0]

            def fun(p, t):
                return self.function(p[0], p[1], t)

            legendEntry = None
            if legend:
                legendEntry = "x₁, x₂ = {0}, {1}".format(x, y)
            if len(tNegative) > 0:
                output = integrate.odeint(fun, [x, y], tNegative)
                plt.plot(output[:, 0], output[:, 1], color=color)

            if len(tPositve) > 0:
                output = integrate.odeint(fun, [x, y], tPositve)
                plt.plot(output[:, 0], output[:, 1], color=color, label=legendEntry)

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

        current_handles, current_labels = plt.gca().get_legend_handles_labels()
        if len(current_labels) > 0:
            plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.15), ncol=3, fancybox=True, prop={'size': 10},
                       markerscale=0.5)

        for point in self.points:
            x, y, color, label = point
            plt.plot(x, y, 'o', color=color, label=label)

        ax.xaxis.set_label_coords(1.05, 0.5)
        ax.yaxis.set_label_coords(0.5, 1.02)
        plt.xlabel('x₁', fontsize=11)
        plt.ylabel('x₂', fontsize=11, rotation='horizontal')
        plt.savefig(filename, dpi=100, bbox_inches='tight')


def run():
    ode = ODEPlot(lambda x, y: -x + y, lambda x, y: -y, (-10, 10), (-10, 10))
    ode.addPoint(0, 0, 'black')
    ode.addInitalStartConditons(2, 2, 'black')
    ode.save('test.png')


run()
