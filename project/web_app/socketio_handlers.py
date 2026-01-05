from flask import request
from flask_socketio import emit

from project.web_app import socketio
from project.web_app.modules import information

import matplotlib.pyplot as plt
import io, sys, base64, queue, threading, builtins, importlib

clients = {}

@socketio.on("connect")
def test_connect():
    print("🔥 SOCKET CONECTADO:", request.sid)

@socketio.on("input")
def handle_input(data):
    sid = request.sid
    if sid in clients:
        clients[sid]["input_queue"].put(data.strip())


@socketio.on("start_exercise")
def start_exercise(data):
    folder_name = data.get("folder_name")
    exercise_id = int(data.get("exercise_id"))

    modulo = next(
        (m for m in information() if m["folder_name"] == folder_name),
        None
    )

    if not modulo:
        emit("output", "Módulo no encontrado\r\n")
        return

    module_path, func_name = modulo["module_menu"].rsplit(".", 1)
    imported_module = importlib.import_module(module_path)
    submenu_func = getattr(imported_module, func_name)

    exercises = submenu_func()

    if exercise_id < 1 or exercise_id > len(exercises):
        emit("output", "Ejercicio inválido\r\n")
        return

    exercise_func = exercises[exercise_id - 1]["exercise"]

    # 🔒 Validación clave
    if not callable(exercise_func):
        emit("output", "[ERROR] El ejercicio no es ejecutable\r\n")
        return

    sid = request.sid
    input_queue = queue.Queue()
    output_queue = queue.Queue()

    clients[sid] = {
        "input_queue": input_queue,
        "output_queue": output_queue
    }

    threading.Thread(
        target=run_exercise_with_graph,
        args=(exercise_func, sid, input_queue, output_queue),
        daemon=True
    ).start()

    def streamer():
        while True:
            msg = output_queue.get()
            if msg is None:
                socketio.emit("end", room=sid)
                break
            socketio.emit("output", msg, room=sid)

    threading.Thread(target=streamer, daemon=True).start()


def run_exercise(func, sid, input_queue, output_queue):
    real_input = builtins.input
    real_print = builtins.print
    real_stdout = sys.stdout

    sys.stdout = io.StringIO()

    def fake_input(prompt=""):
        out = sys.stdout.getvalue()
        if out:
            output_queue.put(out.replace("\n", "\r\n"))
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

        if prompt:
            output_queue.put(prompt.replace("\n", "\r\n"))

        return input_queue.get()

    def fake_print(*a, **k):
        if "file" not in k:
            k["file"] = sys.stdout
        real_print(*a, **k)

    builtins.input = fake_input
    builtins.print = fake_print

    try:
        func()
        remaining = sys.stdout.getvalue()
        if remaining:
            output_queue.put(remaining.replace("\n", "\r\n"))
    except Exception as e:
        output_queue.put(f"[ERROR] {e}\r\n")
    finally:
        builtins.input = real_input
        builtins.print = real_print
        sys.stdout = real_stdout
        output_queue.put(None)


def run_exercise_with_graph(func, sid, input_queue, output_queue):
    real_show = plt.show

    def fake_show():
        buf = io.BytesIO()
        plt.savefig(buf, format="png", dpi=120)
        plt.close()
        buf.seek(0)
        img_b64 = base64.b64encode(buf.read()).decode()
        socketio.emit("graph", img_b64, room=sid)

    plt.show = fake_show
    run_exercise(func, sid, input_queue, output_queue)
    plt.show = real_show
