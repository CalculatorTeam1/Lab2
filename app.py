from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expr = data.get('expression', '')
    try:
        result = eval(expr)
        return jsonify({'result': result})
    except Exception:
        return jsonify({'error': 'ERROR'})


if __name__ == '__main__':
    app.run(debug=True)
