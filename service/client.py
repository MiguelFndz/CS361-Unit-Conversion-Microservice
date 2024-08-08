import zmq
context = zmq.Context()

print("Client attempting to connect to server...")

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print(f"Sending a request...")
amount = input("What is the amount you want to have converted? Do not include units.\n")
unit_from = input("Which unit are you converting from? Possible units are [tsp, tbsp, c, pt, qt, gal, fl oz, mL, L] for volume or [lb, oz, g, kg] for weight\n")
unit_to = input("Which unit do you want to convert to?\n")
socket.send_json({
    "amount": amount,
    "unit_from": unit_from,
    "unit_to": unit_to
})
message = socket.recv_string()
print(f"Server sent back: {message}")

socket.send_string("Q")