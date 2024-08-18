import socket

def check_connection(hostname, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt
        s.settimeout(10)
        
        # Attempt to connect to the server
        s.connect((hostname, port))
        
        # If successful, print a success message
        print(f"Successfully connected to {hostname} on port {port}")
        
        # Close the connection
        s.close()
        
    except socket.error as e:
        # If there is an error, print an error message
        print(f"Failed to connect to {hostname} on port {port}: {e}")

if __name__ == "__main__":
    # Specify the hostname and port you want to connect to
    hostname = "netflix.com"
    port = 443
    
    # Call the function to check the connection
    check_connection(hostname, port)
