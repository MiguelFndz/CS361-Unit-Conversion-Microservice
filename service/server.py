import zmq
from convert import convert


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
while True:
    message = socket.recv_json()
    print(f"received message from the client: {message}")
    if len(message) > 0:
        socket.send_string(str(convert(message)))
        
context.destroy()
        
            



