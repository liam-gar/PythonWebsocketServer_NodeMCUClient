from flask import Flask
from flask_socketio import SocketIO, emit, send
from datetime import datetime

##### Specific Versions needed
# Flask-SocketIO==4.3.1
# python-engineio==3.13.2
# python-socketio==4.6.0

# Initialize SocketIO server
app = Flask(__name__) 
socketio = SocketIO(app, cors_allowed_origins="*")


def send_simulation_date():
    """
    Function to send simulation date to clients
    """
    date = input('Enter Simulation Date: ')
    socketio.emit('date', date)

def send_percentage_of_max_output(output):
    """
    Function to send percentage of max client output needed
    """
    socketio.emit('percent_max_output', output)
    

@socketio.on('connect')
def connected(sio):
    """
    Connect Event
    """
    print(f'Client {sio} connected')
    
    send_simulation_date()

    
@socketio.on('disconnect')
def disconnected(sio):
    """
    Disconnect Event
    """
    print(f'Client {sio} disconnected')


@socketio.on('output_value')
def recieve_client_output(msg):
    """
    Recieve Hourly output from each client
    """
    print(f'Recieved Output: {msg}')

    send_percentage_of_max_output(50)


if __name__=="__main__":
    
    print("Starting server on port 5001")
    socketio.run(app, host="0.0.0.0", port=5001, debug=True)
