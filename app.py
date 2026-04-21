from flask import Flask

app = Flask(__name__)

# VULNERABILITY: Hardcoded Password!
db_password = "SuperSecretAdminPassword123!"
db_user = "admin"

@app.route('/')
def home():
    return "Connected to the database!"

if __name__ == '__main__':
    app.run(debug=True)
