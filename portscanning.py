import socket

def scan_ports(target, start_port, end_port):
    # Loop through specified range of ports
    for port in range(start_port, end_port + 1):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout to handle non-responsive ports
        s.settimeout(1)
        # Attempt to connect to the target on the current port
        result = s.connect_ex((target, port))
        # Check if the connection was successful
        if result == 0:
            print(f"Port {port} is open")
        # Close the socket
        s.close()

# Define the target IP address and range of ports to scan
target_ip = "127.0.0.1"  # Change this to the IP you want to scan
start_port = 1
end_port = 1000  # Adjust the end port range as needed

# Call the function to scan ports
scan_ports(target_ip, start_port, end_port)
