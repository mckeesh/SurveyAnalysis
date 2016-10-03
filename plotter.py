import matplotlib.pyplot as plt
import numpy as np
from OutputWriter import OutputWriter

class Plotter:

	@staticmethod
	def plotMultiLineChart(seriesList, legend):
		for series in seriesList:
			plt.plot(series)
		
		plt.legend(legend, loc='upper center', fancybox=True, shadow=True, ncol = int(len(seriesList)/3))

	@staticmethod
	def savePlot(path):
		dirPath = "/".join(path.split("/")[:-1])
		OutputWriter.createDir(dirPath)
		plt.savefig(path)