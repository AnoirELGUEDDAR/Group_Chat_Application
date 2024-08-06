How it Works (Simplified):

Server Script (server.py):

Binds to a specific IP address and port (localhost, 9999).
Creates two threads:
receive: Continuously listens for incoming messages from clients and adds them to the queue.
broadcast: Takes messages from the queue and sends them to all connected clients.
Client Script (client.py):

Binds to a random port between 8000 and 9000.
Gets the user's nickname.
Creates a thread:
receive: Continuously listens for incoming messages and prints them to the console.
Sends a welcome message to the server.
Enters a loop where the user can type and send messages.
Potential Enhancements:

Encryption: Add encryption to secure message transmission.
Error Handling: Implement more robust error handling to deal with network issues.
User Interface: Create a graphical user interface (GUI) for a more user-friendly experience.
Direct Messaging: Allow users to send private messages to specific individuals.
