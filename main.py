from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.fairino_control import FairinoControl

app = Flask(__name__)
CORS(app, resources=r"/*")  # all origins
# CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})
# CORS(app, origins=["http://localhost:3000"])
# CORS(app, resources={r"/card/*": {"origins": ["http://localhost:3000"]}})
# CORS(app, resources={r"/name/*": {"origins": ["http://localhost:3000"]}})
api = Api(app)

# ROUTE CONFIG
api.add_resource(FairinoControl, "/fairino-control:<string:command>/")
# ROUTE CONFIG

if __name__ == "__main__":
    app.run(debug=True)
