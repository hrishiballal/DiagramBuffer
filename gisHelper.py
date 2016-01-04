import json
import logging
from shapely.geometry.base import BaseGeometry
from shapely.geometry import shape, mapping, shape, asShape
from shapely.geometry import MultiPolygon, MultiPoint, MultiLineString
from shapely import speedups
import shapelyHelper

class GISFactory():
	''' A class to conduct basic (6) GIS operations during copy diagrams. ''' 

	def genFeature(self, geom, allGeoms, errorCounter):
		try:
			curShape = asShape(geom)
			allGeoms.append(curShape)
		except Exception as e:
			logging.error(explain_validity(curShape))
			errorCounter+=1
		return allGeoms, errorCounter

	def bufferLines(self, inputFeats, bufferLength):
		bufferedGeoms =[]
		for curInputFeat in inputFeats:
			cf ={}
			bf = curInputFeat.buffer(bufferLength)
			j = json.loads(shapelyHelper.export_to_JSON(bf))
			cf['type']= 'Feature'
			cf['properties']= {}
			cf['geometry']= j
			bufferedGeoms.append(cf)

		return bufferedGeoms

	def processGeoms(self, inputGeoms, operation, distance,units):
		allGeoms =[]
		errorCounter =0
		for curFeature in inputGeoms['features']:
			allGeoms, errorCounter = self.genFeature(curFeature['geometry'],allGeoms, errorCounter)
		#all geometries are now features. 
		if (operation =='buffer'):
			buf = float(int(distance)/100000.0)
			newGeoms = self.bufferLines(allGeoms, buf)
		
		transformedGeoms = {}
		transformedGeoms['type'] = 'FeatureCollection'
		transformedGeoms['features'] = newGeoms

		return transformedGeoms
