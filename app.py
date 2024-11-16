from flask import Flask
from flask import render_template
from flask import request
import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci(r"./engine/august3.exe")

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("august3.html")


@app.route("/make_move", methods=["POST"])
def make_move():
    fen = request.form.get("fen")

    board = chess.Board(fen)

    result = engine.play(board, chess.engine.Limit(time=0.1))

    board.push(result.move)

    extractFen = board.fen()

    return {"fen": extractFen, "best_move": str(result.move)}


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
