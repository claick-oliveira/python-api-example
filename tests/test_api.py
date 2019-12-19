from python_api.api import app
import json


class TestTransactions():
    def test_index(self):
        '''
        This function does a GET on the path / and
        validate if the response body has data and the status code.

        Test:
            data['msg'] == 'Python API example!'
            data['status'] == 200
            response.status_code == 200
        '''
        response = app.test_client().get(
            '/',
            content_type='application/json'
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data['msg'] == 'Python API example!'
        assert data['status'] == 200

    def test_get(self):
        '''
        This function does a GET on the path /api/unicorns and
        validate if the response body has data and the status code.

        Test:
            len(data['unicorns']) == 10
            response.status_code == 200
        '''
        response = app.test_client().get(
            '/api/unicorns',
            content_type='application/json'
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert len(data['unicorns']) == 10

    def test_get_id(self):
        '''
        This function does a GET on the path /api/unicorns/1 and
        validate if the response body has data and the status code.

        Test:
            response.status_code == 200
            len(data['unicorn']) == 5
            data['unicorn']['id'] == 1
            data['unicorn']['name'] != ''
            data['unicorn']['location'] != ''
            data['unicorn']['info'] != ''
            data['unicorn']['description'] != ''
        '''
        response = app.test_client().get(
            '/api/unicorns/1',
            content_type='application/json'
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert len(data['unicorn']) == 5
        assert data['unicorn']['id'] == 1
        assert data['unicorn']['name'] != ''
        assert data['unicorn']['location'] != ''
        assert data['unicorn']['info'] != ''
        assert data['unicorn']['description'] != ''

    def test_get_id_404(self):
        '''
        This function does a GET on the path /api/unicorns/404 and
        validate if the response body has data and the status code.

        Test:
            response.status_code == 404
            data['error'] == 'Not found'
        '''
        response = app.test_client().get(
            '/api/unicorns/404',
            content_type='application/json'
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 404
        assert data['error'] == 'Not found'

    def test_post(self):
        '''
        This function does a POST on the path /api/unicorns to add a
        new unicorn, a GET on the path /api/unicorns/<id> and validate
        if the data was added.

        Test:
            POST:
            response_post.status_code == 201
            len(data_post['unicorn']) == 5
            data_post['unicorn']['name'] == 'Test Unicorn'
            data_post['unicorn']['location'] == 'Test'
            data_post['unicorn']['info'] == ''
            data_post['unicorn']['description'] == 'Test unicorn was added!'

            GET:
            response_get.status_code == 200
            len(data_post['unicorn']) == 5
            data_get['unicorn']['id'] == data_post['unicorn']['id']
            data_get['unicorn']['name'] == 'Test Unicorn'
            data_get['unicorn']['location'] == 'Test'
            data_get['unicorn']['info'] == ''
            data_get['unicorn']['description'] == 'Test unicorn was added!'
        '''
        response_post = app.test_client().post(
            '/api/unicorns',
            data=json.dumps({
                'name': 'Test Unicorn',
                'location': 'Test',
                'description': 'Test unicorn was added!',
                'info': ''
            }),
            content_type='application/json',
        )

        data_post = json.loads(response_post.get_data(as_text=True))

        response_get = app.test_client().get(
            '/api/unicorns/' + str(data_post['unicorn']['id']),
            content_type='application/json')
        data_get = json.loads(response_get.get_data(as_text=True))

        assert response_post.status_code == 201
        assert len(data_post['unicorn']) == 5
        assert data_post['unicorn']['name'] == 'Test Unicorn'
        assert data_post['unicorn']['location'] == 'Test'
        assert data_post['unicorn']['info'] == ''
        assert data_post['unicorn']['description'] == 'Test unicorn was added!'
        assert response_get.status_code == 200
        assert len(data_post['unicorn']) == 5
        assert data_get['unicorn']['id'] == data_post['unicorn']['id']
        assert data_get['unicorn']['name'] == 'Test Unicorn'
        assert data_get['unicorn']['location'] == 'Test'
        assert data_get['unicorn']['info'] == ''
        assert data_get['unicorn']['description'] == 'Test unicorn was added!'

    def test_put(self):
        '''
        This function does a PUT on the path /api/unicorns to update a
        some unicorn, a GET on the path /api/unicorns/<id> and validate
        if the data was updated.

        Test:

            PUT:
            response_post.status_code == 201
            len(data_post['unicorn']) == 5
            data_post['unicorn']['name'] == 'Test Unicorn'
            data_post['unicorn']['location'] == 'Test'
            data_post['unicorn']['info'] == ''
            data_post['unicorn']['description'] == 'Test unicorn was added!'

            GET:
            response_put.status_code == 200
            len(data_post['unicorn']) == 5
            data_put['unicorn']['id'] == data_post['unicorn']['id']
            data_put['unicorn']['name'] == 'Put Unicorn'
            data_put['unicorn']['location'] == 'Put'
            data_put['unicorn']['info'] == ''
            data_put['unicorn']['description'] == 'Put unicorn was added!'
        '''
        response_post = app.test_client().post(
            '/api/unicorns',
            data=json.dumps({
                'name': 'Test Unicorn',
                'location': 'Test',
                'description': 'Test unicorn was added!',
                'info': ''
            }),
            content_type='application/json',
        )

        data_post = json.loads(response_post.get_data(as_text=True))

        response_put = app.test_client().put(
            '/api/unicorns/' + str(data_post['unicorn']['id']),
            data=json.dumps({
                'name': 'Put Unicorn',
                'location': 'Put',
                'description': 'Put unicorn was added!',
                'info': ''
            }),
            content_type='application/json',
        )
        data_put = json.loads(response_put.get_data(as_text=True))

        assert response_post.status_code == 201
        assert len(data_post['unicorn']) == 5
        assert data_post['unicorn']['name'] == 'Test Unicorn'
        assert data_post['unicorn']['location'] == 'Test'
        assert data_post['unicorn']['info'] == ''
        assert data_post['unicorn']['description'] == 'Test unicorn was added!'
        assert response_put.status_code == 200
        assert len(data_post['unicorn']) == 5
        assert data_put['unicorn']['id'] == data_post['unicorn']['id']
        assert data_put['unicorn']['name'] == 'Put Unicorn'
        assert data_put['unicorn']['location'] == 'Put'
        assert data_put['unicorn']['info'] == ''
        assert data_put['unicorn']['description'] == 'Put unicorn was added!'

    def test_delete(self):
        '''
        This function does a POST on the path /api/unicorns to add a
        new unicorn, a DELETE on the path /api/unicorns/<id> and validate
        if the data was deleted.

        Test:

            POST:
            response_post.status_code == 201
            len(data_post['unicorn']) == 5
            data_post['unicorn']['name'] == 'Test Unicorn'
            data_post['unicorn']['location'] == 'Test'
            data_post['unicorn']['info'] == ''
            data_post['unicorn']['description'] == 'Test unicorn was added!'

            DELETE:
            response_put.status_code == 200
            data_put['result'] == True
        '''
        response_post = app.test_client().post(
            '/api/unicorns',
            data=json.dumps({
                'name': 'Test Unicorn',
                'location': 'Test',
                'description': 'Test unicorn was added!',
                'info': ''
            }),
            content_type='application/json'
        )

        data_post = json.loads(response_post.get_data(as_text=True))

        response_put = app.test_client().delete(
            '/api/unicorns/' + str(data_post['unicorn']['id']),
            content_type='application/json'
        )
        data_put = json.loads(response_put.get_data(as_text=True))

        assert response_post.status_code == 201
        assert len(data_post['unicorn']) == 5
        assert data_post['unicorn']['name'] == 'Test Unicorn'
        assert data_post['unicorn']['location'] == 'Test'
        assert data_post['unicorn']['info'] == ''
        assert data_post['unicorn']['description'] == 'Test unicorn was added!'
        assert response_put.status_code == 200
        assert data_put['result']
