from flask import Flask, jsonify
from views import views


app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

users = [
    {1: "aaron"},
    {2: "drew"},
    {3: "chris"},
]


# GET request to get all users
@app.route("/get_users", methods=["GET"])
def get_users():
    """
    Gets all users
    :return: return JSON
    """
    return jsonify({"users": users})


# GET request for a single user
@app.route("/get_user/<name>", methods=["GET"])
def get_user(name: str):
    """
    Gets a JSON of a user by user_id
    :return: JSON
    """
    name = str(name).lower()
    for user in users:
        for key, value in user.items():
            if value == name:
                return jsonify({"user": user})
    return jsonify({"Error": "User not found"})


# POST request to add a new user
@app.route("/create_user/<user_id>/<name>", methods=["POST", "GET"])
def create_user(user_id: int, name: str):
    """
    Creates a user with the supplied user_id and name
    :return: JSON
    """
    # in the real world, I would check if the user already exists,
    # but just for this example I will add anyway
    user_id = int(user_id)
    name = str(name).lower()
    users.append({user_id: name})
    return jsonify({"message": "User added successfully"})


# PUT request to update an existing user
@app.route("/update_user/<user_id>/<name>", methods=["PUT", "GET"])
def update_user(user_id: int, name: str):
    """
    Updates an existing users name by id
    :return: JSON
    """
    user_id = int(user_id)
    name = name.lower()

    for user in users:
        for key, value in user.items():
            if key == user_id:
                user[key] = name
                return jsonify({"message": "User updated successfully"})
    return jsonify({"Error": "User not found"})


# DELETE request to delete a user
@app.route("/delete_user/<user_id>", methods=["DELETE", "GET"])
def delete_user(user_id: int):
    """
    Deletes an existing user by user_id
    :return: JSON
    """
    user_id = int(user_id)
    for user in users:
        for key in list(user.keys()):
            if key == user_id:
                users.remove(user)
                return jsonify({"message": "User deleted successfully"})
    return jsonify({"Error": "User not found"})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
