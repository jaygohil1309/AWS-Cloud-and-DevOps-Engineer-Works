"""

Example:- 1) Using Variables to Store and Manipulate Configuration Data in a DevOps Context
             In a DevOps context, you often need to manage configuration data for various services or environments. Variables are essential for this purpose. Let's consider a scenario where we need to store and manipulate configuration data for a web server.

"""

# Define configuration variables for a web server.....

server_name = "my_server"
port = 80
is_https_enable = True
max_connections = 1000

# Print the configuration.....

print(f"Server name: {server_name}")
print(f"Port : {port}")
print(f"HTTPS Enabled: {is_https_enable}")
print(f"Max Connections: {max_connections}")

# Update configuration values.....

port = 443
is_https_enable = False

# Print the updated configuration.....

print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enable}")

"""

*** 

"""