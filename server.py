from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<name>')
def calling_name(name):
    return f'hi {name}'

@app.route('/repeat/<int:times_repeat>/<string:input>')
def repeat_string(times_repeat,input):
    if input == 'hello':
        return input*times_repeat
    elif input == 'bye':
        return input*times_repeat
    elif input == 'dogs':
        return input*times_repeat
    else:
        return 'Sorry! No response. Try again.'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

