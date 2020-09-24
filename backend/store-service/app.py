import redis
import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
@app.route('/tasks/<id>', methods=['POST'])
def tasks(id=None):
    r = redis.Redis()
    if request.method == 'POST' and id is not None:
        r.set(f'tasks:{id}', json.dumps(request.form))
        return { 'kind': 'tasks-add', 'code': 'SUCCESS' }
    elif request.method == 'GET':
        results = []
        for key in r.scan_iter("tasks:*"):
            results.append(json.loads(r.get(key).decode()))
        return { 'kind': 'tasks', 'code': 'SUCCESS', 'task': results }
    else:
        return { 'kind': 'error', 'code': 'UNRECOGNIZED' }


 