import zmq
context = zmq.Context()

print("Client attempting to connect to server...")

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print(f"Sending a request...")
socket.send_json(
    {
        "amount": "2",
        "unit_from": "gal",
        "unit_to": "qt"
    }
)

message = socket.recv_string()
print(f"Server sent back: {message}")

socket.send_string("Q")