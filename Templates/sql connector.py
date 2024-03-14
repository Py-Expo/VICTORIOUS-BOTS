import mysql.connector as ms

# Connect to the MySQL database
connection = ms.connect(host="localhost", user="root", password="victorious@123", database="HelpMe")

# Create a cursor object
cursor = connection.cursor()

# Execute a query
cursor.execute("DESC login")

# Fetch the results
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)

# Close the cursor and connection
cursor.close()
connection.close()
