from flask import (
    Flask, jsonify, make_response, abort, request, url_for
)
from load import unicorns

app = Flask(__name__)


def make_public_unicorn(unicorn):
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


@app.route('/')
def index():
    return jsonify({
        'msg': 'Python API example!',
        'status': 200
    })


@app.route('/api/unicorns', methods=['GET'])
def get_unicorns():
    return jsonify(
        {'unicorns': [make_public_unicorn(unicorn) for unicorn in unicorns]}
    )


@app.route('/api/unicorns/<int:unicorn_id>', methods=['GET'])
def get_unicorn(unicorn_id):
    unicorn = [unicorn for unicorn in unicorns if unicorn['id'] == unicorn_id]
    if len(unicorn) == 0:
        abort(404)
    return jsonify({'unicorn': unicorn[0]})


@app.route('/api/unicorns', methods=['POST'])
def create_task():
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
    unicorn = [unicorn for unicorn in unicorns if unicorn['id'] == unicorn_id]
    if len(unicorn) == 0:
        abort(404)
    unicorns.remove(unicorn[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# TODO:
# Create environment variable to turn on/off debug
if __name__ == '__main__':
    app.run(host='0.0.0.0')
