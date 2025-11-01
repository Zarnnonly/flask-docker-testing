from flask import Flask

# Bikin aplikasi Flask
app = Flask(__name__)

# Route untuk halaman utama
@app.route("/")
def home():
    return "<h1>Hello, World from Zahrand!</h1>"

# Route kedua buat latihan
@app.route("/about")
def about():
    return "<h1>This is About page</h1><p>This is my first Docker implementation</p>"

# Jalankan aplikasi
if __name__ == "__main__":
    # host='0.0.0.0' penting biar bisa diakses dari luar container
    app.run(host='0.0.0.0', port=5000, debug=True)
