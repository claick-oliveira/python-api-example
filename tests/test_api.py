from python_api.api import app
import json


class TestTransactions():
    def test_index(self):
        response = app.test_client().get(
            '/',
            content_type='application/json'
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data['msg'] == 'Python API example!'
        assert data['status'] == 200

    def test_get(self):
        response = app.test_client().get(
            '/api/unicorns',
            content_type='application/json'
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert len(data['unicorns']) == 10

    def test_get_id(self):
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
        response = app.test_client().get(
            '/api/unicorns/404',
            content_type='application/json'
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 404
        assert data['error'] == 'Not found'

    def test_post(self):
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
