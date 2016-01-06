import gisHelper, requests, json
# A sample script to take a diagram from Geodesign Hub, buffer it and send
# it back as a new diagram using the API.
#
API_URL = 'https://www.geodesignhub.com/api/v1/'

USER_TOKEN = '5d72a5465bc8a61bb6dd02457cbf97150735bfbf' # can be accessed here: https://www.geodesignhub.com/api/token/
PROJECT_ID = '229658795739b07b'  # e.g. 68c456b961e617e1


class APIHelper():

	def __init__(self):
		self.projectid = PROJECT_ID
		self.token = USER_TOKEN
		self.securl = API_URL

	def getDiagramGeoms(self, diagid):
		''' Create a requests object with correct headers and creds. '''
		securl = self.securl+ 'projects'+ '/' + self.projectid + '/' +'diagrams' + '/'+ str(diagid) +'/'
		headers = {'Authorization': 'Token '+ self.token}
		r = requests.get(securl, headers=headers)
		return r

	def submitUpload(self,geoms, projectorpolicy, featuretype, description, reqid ):
		''' Create a requests object with correct headers and creds. '''
		securl = self.securl+ 'projects'+ '/' + self.projectid + '/' +'requirements'+'/'+ str(reqid) + '/'+ 'add' +'/' + projectorpolicy +'/'
		headers = {'Authorization': 'Token '+ self.token, 'content-type': 'application/json'}
		postdata = {'geometry':geoms, 'description':description, 'featuretype':featuretype}
		r = requests.post(securl, headers= headers, data = json.dumps(postdata))
		return r

if __name__ == "__main__":
	diagID = 32 # diagram to be downloaded
	operation = 'buffersubtract' # GIS operation
	distance = 100 # distance of buffer
	units = 'm' # units
	myAPIHelper = APIHelper()
	# the id of the diagram that needs to be transformed as a part of GIS operation.
	r = myAPIHelper.getDiagramGeoms(diagID)
	print r.status_code
	if r.status_code == 200:
		op = json.loads(r.text)
		geoms = op['geojson']
		myGISHelper = gisHelper.GISFactory()
		transformedFC = myGISHelper.processGeoms(geoms, operation, distance, units)
		# print json.dumps(transformedFC)
		upload = myAPIHelper.submitUpload(geoms = transformedFC, projectorpolicy= 'policy',featuretype = 'polygon', description= 'Subtracted buffer', reqid = 2 )
		print upload.text
