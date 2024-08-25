from flask import Flask, request, redirect
import mysql.connector
import hashlib
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

def get_db_connection():
    """
    Create a connection to the MySQL database on RDS.
    """
    connection = mysql.connector.connect(
        host='database-1.cb6gkjpgnqy9.us-east-1.rds.amazonaws.com',
        user='admin',
        password='stairwaytoheaven',  # Replace with your RDS password
        database='dating_site'  # Replace with your actual database name
    )
    return connection

@app.route('/result', methods=['POST'])
def register():
    logging.debug("Received form data: %s", request.form)
    
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    gender = request.form.get('gender')
    relationship_status = request.form.get('relationshipStatus')
    gender_preference = request.form.get('genderPreference')

    # Validate inputs
    if not name or not email or not password:
        return "All fields are required", 400

    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to the RDS database
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # SQL query to insert user data into the database
            sql = """
                INSERT INTO users (name, gender, relationship_status, gender_preference, email, password)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (name, gender, relationship_status, gender_preference, email, hashed_password))
            connection.commit()
            logging.debug("Data inserted successfully.")
    except Exception as e:
        logging.error("Error inserting data: %s", e)
        return "An error occurred while inserting data.", 500
    finally:
	connection.close()

    # Redirect to the result page with query parameters
    return redirect(f'/result.html?name={name}&gender={gender}&relationshipStatus={relationship_status}&genderPreference={gender_preference}')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


