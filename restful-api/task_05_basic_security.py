from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()

# JWT üçün gizli açar (Real layihələrdə bu çox uzun və gizli olmalıdır)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# İstifadəçilərin bazası (Yaddaşda saxlanılır)
# Şifrələri heç vaxt açıq saxlamırıq, 'generate_password_hash' ilə şifrələyirik.
users = {
    "user1": {
        "username": "user1", 
        "password": generate_password_hash("password"), 
        "role": "user"
    },
    "admin1": {
        "username": "admin1", 
        "password": generate_password_hash("password"), 
        "role": "admin"
    }
}

# --- BASIC AUTHENTICATION SETUP ---

@auth.verify_password
def verify_password(username, password):
    """
    Basic Auth üçün şifrə yoxlanışı.
    İstifadəçi adı varmı və şifrə hash-i uyğundurmu?
    """
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Basic Auth ilə qorunan marşrut.
    """
    return "Basic Auth: Access Granted"

# --- JWT ERROR HANDLERS (Tapşırıq tələbi: Hamısı 401 qaytarmalıdır) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

# --- JWT AUTHENTICATION SETUP ---

@app.route('/login', methods=['POST'])
def login():
    """
    Giriş funksiyası.
    İstifadəçi adı və şifrə doğru olarsa, JWT token qaytarır.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        # Token yaradılır (kimliyi username olaraq saxlayırıq)
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    JWT Token ilə qorunan marşrut.
    """
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Yalnız Admin rolu olanlar üçün marşrut.
    """
    # Token-in içindən istifadəçi adını alırıq
    current_user = get_jwt_identity()
    
    # Həmin istifadəçinin rolunu yoxlayırıq
    if users[current_user]["role"] == "admin":
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403

if __name__ == '__main__':
    app.run(debug=True)
