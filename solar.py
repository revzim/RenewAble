#!/usr/bin/python

class Structure(object):
	"""A structure is any object which the solar panel can be placed and contain the 
	following properties

	Attrs:
		name: simple name for the structure
		length: the length of the structure in mm
		width: the width of the structure in mm
		angle: if top of structure (roof) has an angle
	"""

	def __init__(self, name, length, width, height, angle):
		#Return a Structure obj
		self.name = name
		self.length = length
		self.width = width
		self.height = height
		self.angle = angle

	def calculate_area(self):
		return self.length * self.width

	def calculate_volume(self):
		return self.length * self.width * self.height

	def amount_fit_w(self, sp_width):
		s_length = self.length
		amt = s_length / sp_width
		return amt

	def amount_fit_l(self, sp_length):
		s_length = self.length
		amt = s_length / sp_length
		return amt

	def details(self):
		return "Name: {0}\nLength: {1}mm\nWidth: {2}mm\nHeight: {3}mm\nAngle of Surface: {4} degrees".format(self.name, self.length, self.width, self.height, self.angle)

class SolarPanel(object):
	"""A SolarPanel is any solar panel object

	Attrs:
		name: name of company type solarpanel
		model: model name of the solar panel
		length: the length of the solar panel in mm
		width: the width of the solar panel in mm
		cells: amount of cells in solar panel
	"""

	def __init__(self, name, model, length, width, height, cells):
		#Return a Structure obj
		self.name = name
		self.model = model
		self.length = length
		self.width = width
		self.height = height
		self.cells = cells

	def calculate_area(self):
		return self.length * self.width

	def calculate_volume(self):
		return self.length * self.width * self.height

	def get_cells(self):
		return self.cells

	def details(self):
		return "Name: {0}\nModel: {1}\nLength:{2}mm\nWidth: {3}mm\nHeight: {4}mm\nCells: {5}".format(self.name, self.model, self.length, self.width, self.height, self.cells)
class Battery(object):
	"""A battery is a storage device for the solar power that will be stored.
	
	Attrs:
		name: name of battery with company
		model: model of the battery
		mass: mass of battery in kg
		length: the length of the battery in mm
		width: the width of the battery in mm
		height: the height of the battery in mm
		efficiency: the round trip efficiency of the battery %
		power continuous: the continuous power 
		power peak: the peak power 
		voltage: average voltage produced measured in volts
		current Normal: measured in amps(normal amps)
		current Peak: measured in amps (peak amps)
		temp low: low operating temperature at which it operates in Celsius	
		temp high: high operating temperature at which it operates in Celsius	
	"""
	def __init__(self, name, model, price, mass, length, width, height, efficiency, power_continous, power_peak, voltage, current_normal, current_peak, temp_low, temp_high):
		self.name = name
		self.model = model
		self.price = price
		self.mass = mass
		self.length = length
		self.width = width
		self.height = height
		self.efficiency = efficiency
		self.power_continous = power_continous
		self.power_peak = power_peak
		self.voltage = voltage
		self.current_normal = current_normal
		self.current_peak = current_peak
		self.temp_low = temp_low
		self.temp_high = temp_high

	def calc_area(self):
		return self.width * self.length

	def calculate_volume(self):
		return self.length * self.width * self.height

	def details(self):
		return "Name: {0}\nModel: {1}\nPrice: ${2}\nMass: {3}kg\nLength: {4}mm\nWidth: {5}mm\nHeight: {6}mm\nEfficiency: {7}%\nContinous Power:{8}kW\nPeak Power: {9}kW\nVoltage: {10} volts\nNormal Current: {11}amp\nPeak Current: {12}amp\nLow Operating Temp: {13}C to {14}C".format(self.name, self.model, self.price, self.mass, self.length, self.width, self.height, self.efficiency, self.power_continous, self.power_peak, self.voltage, self.current_normal, self.current_peak, self.temp_low, self.temp_high)

#lirr average train car
lirr = Structure("LIRR Train Car", 25908, 3200.4, 2590.8, 0.0)

#
industrial_solarpanel = SolarPanel("SolarPower Inc.", "Industrial" , 1955.8, 990.6, 45.72, 96)
residential_solarpanel = SolarPanel("SolarPower Inc.", "Residential", 1651, 990.6, 45.72, 72)
tesla_powerwall10kWh = Battery("Tesla Power Wall", "10kWh", 3500, 100, 1300, 860, 180, 92, 2.0, 3.3, 400, 5, 8.5, -20, 43)
tesla_powerwall7kWh = Battery("Tesla Power Wall", "7kWh", 3000, 100, 1300, 860, 180, 92, 2.0, 3.3, 400, 5, 8.5, -20, 43)

print lirr.details() + "\n"
print industrial_solarpanel.details()+ "\n"
print residential_solarpanel.details()+ "\n"
print tesla_powerwall10kWh.details()

#amount_lirr_w_residential = lirr.amount_fit_width(industrial_solarpanel.width, industrial_solarpanel.length)
#amount_lirr_l_residential = lirr.amount_fit_length(industrial_solarpanel.width, industrial_solarpanel.length)
solarpanel_list = [industrial_solarpanel, residential_solarpanel]
for i in solarpanel_list:
	print "\n",i.details()

print "\nThe area available to place the {0}: {1} on top of the {2} is {3}mm".format(industrial_solarpanel.name, industrial_solarpanel.model, lirr.name, lirr.calculate_area())
print "\nThe area available to place the {0}: {1} on top of the {2} is {3}mm".format(residential_solarpanel.name, residential_solarpanel.model, lirr.name, lirr.calculate_area())

print "You can fit {0} {1}: {2} solar panels on top of a {3} by lining them up side by side".format(lirr.amount_fit_w(industrial_solarpanel.width), industrial_solarpanel.name, industrial_solarpanel.model, lirr.name)
print "You can fit {0} {1}: {2} solar panels on top of a {3} by lining them up top by bottom".format(lirr.amount_fit_l(industrial_solarpanel.length), industrial_solarpanel.name, industrial_solarpanel.model, lirr.name)




