from flask import Flask, jsonify


app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Buy groceries", "description":
     "Milk, Cheese, Pizza, Fruit", "done": False},

    {"id": 2, "title": "Learn Python", "description":
     "Need to find a good Python tutorial", "done": False},
]


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
