from flask import (
    Flask, jsonify, make_response, abort, request, url_for
)
from load import unicorns

app = Flask(__name__)


def make_public_unicorn(unicorn):
    '''
    This function adds for each object a uri, this uri is
    a link to access the data, example:

    "uri": "http://<url>/api/unicorns/<id>"

    Parameters:
    unicorn (dict): Dictionary with unicorn data

    Returns:
    new_unicorn (dict): Dictionary with unicorn data + uri for each unicorn
    '''
    new_unicorn = {}
    for field in unicorn:
        if field == 'id':
            new_unicorn['uri'] = (
                url_for('get_unicorn',
                        unicorn_id=unicorn['id'],
                        _external=True)
            )
        else:
            new_unicorn[field] = unicorn[field]
    return new_unicorn


@app.route('/', methods=['GET'])
def index():
    '''
    This function returns a message as json. The method allowed is GET.

    Path:
    /

    Returns:
    {
        'msg': 'Python API example!',
        'status': 200
    }
    '''
    return jsonify({
        'msg': 'Python API example!',
        'status': 200
    })


@app.route('/api/unicorns', methods=['GET'])
def get_unicorns():
    '''
    This function returns all unicorns as json. The method allowed is GET

    Path:
    /api/unicorns

    Returns:
    {
        "unicorns": [
            {
                "description": "The unicornfish, Naso unicornis, has a single,
                hornlike protrusion in the middle of its forehead between its
                eyes, which makes it look like it has a funny little face.",
                "info": "https://en.wikipedia.org/wiki/Naso_(fish)",
                "location": "Pacific Oceans",
                "name": "Unicornfish",
                "uri": "http://0.0.0.0:5000/api/unicorns/1"
            },
            ...N...
        ]
    }
    '''
    return jsonify(
        {'unicorns': [make_public_unicorn(unicorn) for unicorn in unicorns]}
    )


@app.route('/api/unicorns/<int:unicorn_id>', methods=['GET'])
def get_unicorn(unicorn_id):
    '''
    This function returns an unicorns as json based on ID. The method
    allowed is GET

    Path:
    /api/unicorns/<ID>

    Parameters:
    unicorn_id (int): Unicorn ID

    Returns:
    {
        "unicorn": {
            "description": "The unicornfish, Naso unicornis, has a single,
            hornlike protrusion in the middle of its forehead between its
            eyes, which makes it look like it has a funny little face.",
            "id": 1,
            "info": "https://en.wikipedia.org/wiki/Naso_(fish)",
            "location": "Pacific Oceans",
            "name": "Unicornfish"
        }
    }
    '''
    unicorn = [unicorn for unicorn in unicorns if unicorn['id'] == unicorn_id]
    if len(unicorn) == 0:
        abort(404)
    return jsonify({'unicorn': unicorn[0]})


@app.route('/api/unicorns', methods=['POST'])
def create_task():
    '''
    This function adds a new unicorn bases on body. The method allowed is POST

    Path:
    /api/unicorns

    Body:
    {
        "name": "New Unicorn",
        "location": "Rainbow",
        "description": "New unicorn was added!",
        "info": ""
    }

    Returns:
    {
        "unicorn": {
            "description": "New unicorn was added!",
            "id": 11,
            "info": "",
            "location": "Rainbow",
            "name": "New Unicorn"
        }
    }
    '''
    if not request.json or 'name' not in request.json:
        abort(400)
    unicorn = {
        'id': unicorns[-1]['id'] + 1,
        'name': request.json['name'],
        'location': request.json.get('location', ''),
        'description': request.json.get('description', ''),
        'info': request.json.get('info', '')
    }
    unicorns.append(unicorn)
    return jsonify({'unicorn': unicorn}), 201


@app.route('/api/unicorns/<int:unicorn_id>', methods=['PUT'])
def update_task(unicorn_id):
    '''
    This function updates a new unicorn bases on body. The method
    allowed is PUT

    Path:
    /api/unicorns/<ID>

    Parameters:
    unicorn_id (int): Unicorn ID

    Body:
    {
        "name": "New Unicorn",
        "location": "Rainbow",
        "description": "New unicorn was updated!",
        "info": ""
    }

    Returns:
    {
        "unicorn": {
            "description": "New unicorn was updated!",
            "id": 11,
            "info": "",
            "location": "Rainbow",
            "name": "New Unicorn"
        }
    }
    '''
    unicorn = [unicorn for unicorn in unicorns if unicorn['id'] == unicorn_id]
    if len(unicorn) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if ('name' in request.json and type(request.json['name']) is not str):
        abort(400)
    if ('location' in request.json and
            type(request.json['location']) is not str):
        abort(400)
    if ('description' in request.json and
            type(request.json['description']) is not str):
        abort(400)
    if ('info' in request.json and
            type(request.json['info']) is not str):
        abort(400)
    unicorn[0]['name'] = request.json.get('name', unicorn[0]['name'])
    unicorn[0]['location'] = (
        request.json.get('location', unicorn[0]['location'])
    )
    unicorn[0]['description'] = (
        request.json.get('description', unicorn[0]['description'])
    )
    unicorn[0]['info'] = request.json.get('info', unicorn[0]['info'])
    return jsonify({'unicorn': unicorn[0]})


@app.route('/api/unicorns/<int:unicorn_id>', methods=['DELETE'])
def delete_task(unicorn_id):
    '''
    This function deletes an unicorn bases on ID. The method
    allowed is DELETE

    Path:
    /api/unicorns/<ID>

    Parameters:
    unicorn_id (int): Unicorn ID

    Returns:
    {
        "result": true
    }
    '''
    unicorn = [unicorn for unicorn in unicorns if unicorn['id'] == unicorn_id]
    if len(unicorn) == 0:
        abort(404)
    unicorns.remove(unicorn[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    '''
    This function returns a message as json. The method allowed is GET.

    Parameters:
    error (err): Error message

    Returns:
    {
        'error': 'Not found'
    }
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)


# TODO:
# Create environment variable to turn on/off debug
if __name__ == '__main__':
    app.run(host='0.0.0.0')
