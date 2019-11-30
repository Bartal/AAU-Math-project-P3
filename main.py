from ODEPlot import ODEPlot
import numpy as np

Plot1 = ODEPlot(lambda x, y: y, lambda x, y: -x, (-10, 10), (-10, 10))
Plot1.save('Chapter_5_graph_1.png')

Plot1.addInitalStartConditons(0, 2, 'black')
Plot1.addInitalStartConditons(0, 5, 'black')
Plot1.save('Chapter_5_graph_2.png')

Plot2 = ODEPlot(lambda x, y: -x + y, lambda x, y: -y, (-10, 10), (-10, 10))
Plot2.addPoint(0, 0, 'black')
Plot2.addInitalStartConditons(-11, 4, 'black')
Plot2.addInitalStartConditons(-7, 10, 'black')
Plot2.addInitalStartConditons(3, 10, 'black')

Plot2.addInitalStartConditons(11, -4, 'black')
Plot2.addInitalStartConditons(7, -10, 'black')
Plot2.addInitalStartConditons(-3, -10, 'black')
Plot2.save('Chapter_5_graph_3.png')

Plot3 = ODEPlot(lambda x, y: x - y, lambda x, y: y, (-10, 10), (-10, 10))
Plot3.addPoint(0, 0, 'black')
Plot3.addInitalStartConditons(-11, 4, 'black')
Plot3.addInitalStartConditons(-7, 10, 'black')
Plot3.addInitalStartConditons(3, 10, 'black')
Plot3.addInitalStartConditons(11, -4, 'black')
Plot3.addInitalStartConditons(7, -10, 'black')
Plot3.addInitalStartConditons(-3, -10, 'black')
Plot3.save('Chapter_5_graph_4.png')
