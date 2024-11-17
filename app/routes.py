from flask import render_template, request, jsonify

tasks = []

def setup_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html", tasks=tasks)

    @app.route("/add", methods=["POST"])
    def add_task():
        task = request.json.get("task")
        if task:
            tasks.append(task)
            return jsonify({"status": "success", "task": task}), 201
        return jsonify({"status": "error"}), 400

    @app.route("/delete/<int:task_id>", methods=["DELETE"])
    def delete_task(task_id):
        if 0 <= task_id < len(tasks):
            removed_task = tasks.pop(task_id)
            return jsonify({"status": "success", "removed_task": removed_task}), 200
        return jsonify({"status": "error"}), 404

    @app.route("/environment")
    def environment():
        return jsonify({"environment": app.config.get("ENV", "unknown")})