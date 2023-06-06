from flask import Flask, request

app = Flask(__name__)

@app.route("/api/user")
def user_api():
    user_id = request.args.get("user_id")
    # Do something with the user_id
    return "User ID: {}".format(user_id)

if __name__ == "__main__":
    app.run()
