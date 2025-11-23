from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yadda saxlamaq üçün lüğət (In-memory storage)
users = {}

@app.route('/')
def home():
    """
    Ana səhifə (Root endpoint)
    """
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """
    Bütün istifadəçi adlarını (keys) qaytarır.
    """
    # users lüğətinin açarlarını listə çevirib JSON kimi qaytarırıq
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """
    API statusunu yoxlamaq üçün.
    """
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """
    Dinamik marşrut: Konkret bir istifadəçinin məlumatını qaytarır.
    """
    # Əgər istifadəçi varsa, məlumatını qaytar
    if username in users:
        return jsonify(users[username])
    # Yoxdursa, 404 xətası qaytar
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    POST sorğusu ilə yeni istifadəçi əlavə etmək.
    """
    # Gələn məlumatı JSON formatında alırıq
    data = request.get_json()

    # 1. JSON validasiyası (Əgər data yoxdursa)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Username sahəsinin yoxlanması
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. Təkrarçılığın yoxlanması (Duplicate check)
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Hər şey qaydasındadırsa, istifadəçini əlavə edirik
    users[username] = data

    # Uğurlu cavab (Status 201 - Created)
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
