Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Eric Coholan
>>> #GEOG656
>>> #Lab 1
>>> 
>>> class Geometry(object):
	uniqueID = 0
	def __init__(self):
		self.id = Geometry.uniqueID
		Geometry.uniqueID = Geometry.uniqueID + 1

		
>>> class Point(Geometry):
	def __init__(self, x, y):
                Geometry.__init__(self)
		self.x = round(x, 2)
		self.y = round(y, 2)
	def __str__(self):
		return '(%s, %s)'%(self.x, self.y)

	
>>> 
