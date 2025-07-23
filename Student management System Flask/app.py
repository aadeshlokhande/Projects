from flask import Flask
from route import registerRoute
import os

def createApp():
    app = Flask(__name__)    
    app.secret_key = "PythonProgram"
    try:
        registerRoute(app)
    except Exception as e:
        print(f"❌ Critical error in route registration: {e}")
    return app

if __name__ == "__main__":
    os.system("clear")
    app = createApp()
    app.run(debug=True)
