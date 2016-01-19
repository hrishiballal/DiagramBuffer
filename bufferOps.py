import gisHelper, requests, json, GeodesignHub
# A sample script to take a diagram from Geodesign Hub, buffer it and send
# it back as a new diagram using the API.
#

if __name__ == "__main__":
	diagID = 32 # diagram to be downloaded
	operation = 'buffersubtract' # GIS operation
	distance = 100 # distance of buffer
	units = 'm' # units
	myAPIHelper = GeodesignHub.GeodesignHubClient(url = 'http://local.dev:8000/api/v1/', project_id='62ead880b1592bc0', token='5d72a5465bc8a61bb6dd02457cbf97150735bfbf')
	# the id of the diagram that needs to be transformed as a part of GIS operation.
	r = myAPIHelper.get_diagram_geoms(diagID)

	if r.status_code == 200:
		op = json.loads(r.text)
		geoms = op['geojson']
		myGISHelper = gisHelper.GISFactory()
		transformedFC = myGISHelper.processGeoms(geoms, operation, distance, units)
		# print json.dumps(transformedFC)
		upload = myAPIHelper.post_as_diagram(geoms = transformedFC, projectorpolicy= 'policy',featuretype = 'polygon', description= 'Subtracted buffer', reqid = 2 )
		print upload.text
