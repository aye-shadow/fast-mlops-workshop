from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/')
def home():
        """Return"""
        print("I am inside hello world")
        return "Hellow World! I can make change at route: /change"

@app.route('/100/change/<dollar>/<cents>')
def change100route(dollar, cents):
        """Return"""
        print("I am inside change100route")
        return "Hellow World! I can make change at route: /change"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)