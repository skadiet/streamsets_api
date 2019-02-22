import requests
import base64
import getpass
import json

class StreamSetsAPI(object):

    def __init__(self):
        username=raw_input('Username: ')
        password=getpass.getpass()
        self.basic_auth=base64.base64encode('{0}:{1}'.format(username, password))
        self.request_headers=self.constructRequestHeaders()

    def constructRequestHeaders(self):
        d={}
        d['authorization']='Basic {0}'.format(self.basic_auth)
        d['content-type']='application/json'
        d['accept']='application/json'
        d['x-requested-by']='sdc'
        return d

    def getStatus(self):
        url='http://localhost:18630/rest/v1/pipelines/status'
        r=requests.get(url, headers=self.request_headers)
        print r.content

    def getPipelineNames(self):
        self.getStatus()

    def startOnePipeline(self, pipeline_name):
        url='http://localhost:18630/rest/v1/pipeline/{0}/start?rev=0'.format(pipeline_name)
        r=requests.post(url, headers=self.request_headers)
        print r.content

    def stopOnePipeline(self, pipeline_name):
        url='http://localhost:18630/rest/v1/pipeline/{0}/stop?rev=0'.format(pipeline_name)
        r=requests.post(url, headers=self.request_headers)
        print r.content

    def startPipelines(self, pipeline_list):
        if not type(pipeline_list)==list:
            print 'pipeline_list must be a list'
            return
        url='http://localhost:18630/rest/v1/pipelines/start'
        r=requests.post(url, headers=self.request_headers, json=pipeline_list)
        print r.content

    def stopPipelines(self, pipeline_list):
        if not type(pipeline_list)==list:
            print 'pipeline_list must be a list'
            return
        url='http://localhost:18630/rest/v1/pipelines/stop'
        r=requests.post(url, headers=self.request_headers, json=pipeline_list)
        print r.content