from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    tasks.append(task)
    return jsonify({'message': 'Task added successfully'})

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'message': 'Invalid index'})

@app.route('/tasks/<int:index>/complete', methods=['PUT'])
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        return jsonify({'message': 'Task marked as completed'})
    else:
        return jsonify({'message': 'Invalid index'})

if __name__ == '__main__':
    app.run(debug=True)
