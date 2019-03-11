import app
import requests
from flask_restful import Resource
from app.common import build_working_response

class WorkApi(Resource):

    def get(self):

        work_list = []

        #if app.dependency_api.healthcheck():
        #    work_list.append(build_working_response('dependency-api', 'working'))
        #    app.log.info('testing info log')
        #else:
        #    work_list.append(build_working_response('dependency-api', 'error',
        #                                            'dependency-api offline.', 'CODE01'))
        #    app.log.info('testing ERROR log')

        if requests.get('http://www.google.com'):
            work_list.append(build_working_response('google', 'working'))
            app.log.info('testing info log')
        else:
            work_list.append(build_working_response('google',
                                                    'error', 'another_dependency-api offline.', 'CODE02'))
            app.log.info('testing ERROR log')

        try:
            if requests.get('http://localhost:8000') == 200:
                work_list.append(build_working_response('google', 'working'))
                app.log.info('testing info log')
            else:
                work_list.append(build_working_response('google',
                                                        'error', 'another_dependency-api offline.', 'CODE02'))
                app.log.info('testing ERROR log')
        except requests.ConnectionError as e:
            work_list.append(build_working_response('google',
                                                    'error', str(e), 'CODE04'))
            app.log.error(e)
        return work_list, 200
