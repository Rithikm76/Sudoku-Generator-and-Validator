from flask import Flask, request, jsonify, render_template
from two import Sudoku3D
import webbrowser
import threading

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    block_size = data.get('block_size', 3)
    difficulty = data.get('difficulty', 2)
    grid_size = block_size ** 2
    total_cells = grid_size * grid_size
    if difficulty == 1:
        clues = int(total_cells * 0.45)
    elif difficulty == 2:
        clues = int(total_cells * 0.35)
    elif difficulty == 3:
        clues = int(total_cells * 0.25)
    else:
        return jsonify({'error': 'Invalid difficulty'}), 400
    game = Sudoku3D(block_size=block_size)
    game.generate_puzzle(clues=clues)
    return jsonify({'board': game.board, 'block_size': block_size, 'difficulty': difficulty})

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    board = data.get('board')
    block_size = data.get('block_size', 3)
    game = Sudoku3D(block_size=block_size)
    game.board = board
    valid = game.is_solved_correctly()
    return jsonify({'valid': valid})

if __name__ == '__main__':
    def open_browser():
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open('http://localhost:5000')
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True) 