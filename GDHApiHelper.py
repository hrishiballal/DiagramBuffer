import requests, json
# API_URL = 'https://www.geodesignhub.com/api/v1/'
API_URL = 'http://local.dev:8000/api/v1/'

USER_TOKEN = '5d72a5465bc8a61bb6dd02457cbf97150735bfbf' # can be accessed here: https://www.geodesignhub.com/api/token/
PROJECT_ID = '62ead880b1592bc0'  # e.g. 68c456b961e617e1

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

	def addAsDiagram(self,geoms, projectorpolicy, featuretype, description, reqid ):
		''' Create a requests object with correct headers and creds. '''
		securl = self.securl+ 'projects'+ '/' + self.projectid + '/' +'requirements'+'/'+ str(reqid) + '/'+ 'add' +'/' + projectorpolicy +'/'
		headers = {'Authorization': 'Token '+ self.token, 'content-type': 'application/json'}
		postdata = {'geometry':geoms, 'description':description, 'featuretype':featuretype}
		r = requests.post(securl, headers= headers, data = json.dumps(postdata))
		return r

	def submitAsEvaluationJSON(self, geoms, reqid, username=None):
		''' Create a requests object with correct headers and creds. '''
		securl = self.securl+ 'projects'+ '/' + self.projectid + '/' +'requirements'+'/'+ str(reqid) + '/e/json/'
		if username:
			securl += username +'/'
		headers = {'Authorization': 'Token '+ self.token, 'content-type': 'application/json'}

		r = requests.post(securl, headers= headers, data = json.dumps(geoms))
		return r

	def submitAsImpactJSON(self, geoms, reqid, username=None):
		''' Create a requests object with correct headers and creds. '''

		securl = self.securl+ 'projects'+ '/' + self.projectid + '/' +'requirements'+'/'+ str(reqid) + '/i/json/'
		if username:
			securl += username +'/'

		headers = {'Authorization': 'Token '+ self.token, 'content-type': 'application/json'}
		r = requests.post(securl, headers= headers, data = json.dumps(geoms))
		return r

	def submitAsEvaluationGBF(self, geoms, reqid, username=None):
		''' Create a requests object with correct headers and creds. '''
		securl = self.securl+ 'projects'+ '/' + self.projectid + '/' +'requirements'+'/'+ str(reqid) + '/e/gbf/'
		if username:
			securl += username +'/'
		headers = {'Authorization': 'Token '+ self.token}

		r = requests.post(securl, headers= headers, files = {'geoms.gbf':geoms})
		return r

	def submitAsImpactGBF(self, geoms, reqid, username=None):
		''' Create a requests object with correct headers and creds. '''

		securl = self.securl+ 'projects'+ '/' + self.projectid + '/' +'requirements'+'/'+ str(reqid) + '/i/gbf/'
		if username:
			securl += username +'/'
		headers = {'Authorization': 'Token '+ self.token}
		r = requests.post(securl, headers= headers, files = {'geoms.gbf':geoms})
		return r

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
