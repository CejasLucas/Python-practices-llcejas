import io, sys, base64
import queue, threading
import builtins, importlib
import matplotlib.pyplot as plt
# ----------- Flask ------------
from flask import request
from flask_socketio import emit
# ------- Applications ---------
from project.web_app import socketio
from project.web_app.modules import information


clients = {}

def run_exercise(func, sid, input_queue, output_queue):
    real_input = builtins.input
    real_print = builtins.print
    real_stdout = sys.stdout

    sys.stdout = io.StringIO()

    def fake_input(prompt=""):
        out = sys.stdout.getvalue()
        if out:
            output_queue.put(out.replace("\n","\r\n"))
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        if prompt:
            output_queue.put(prompt.replace("\n","\r\n"))
        return input_queue.get()

    builtins.input = fake_input
    builtins.print = lambda *args, **kwargs: real_print(*args, file=sys.stdout, **kwargs)

    try:
        func()
        remaining = sys.stdout.getvalue()
        if remaining:
            output_queue.put(remaining.replace("\n","\r\n"))
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

        plt.savefig(buf, format='png', dpi=120, bbox_inches='tight', pad_inches=0.3)
        plt.close()
        buf.seek(0)

        img_b64 = base64.b64encode(buf.read()).decode('utf-8')
        socketio.emit("graph", img_b64, room=sid)
    plt.show = fake_show
    run_exercise(func, sid, input_queue, output_queue)
    plt.show = real_show


# ----------------------- Handlers of SocketIO -----------------------
@socketio.on("start_exercise")
def start_exercise(data):
    file_name = data.get("file_name")
    exercise_id = int(data.get("exercise_id"))

    modulo = next((m for m in information() if m["file_name"] == file_name), None)
    if not modulo or "submenu_func" not in modulo:
        emit("output", "Ejercicio no encontrado\r\n")
        return

    module_path, func_name = modulo["submenu_func"].rsplit(".", 1)
    imported_module = importlib.import_module(module_path)
    submenu_func = getattr(imported_module, func_name)
    exercises = submenu_func()
    exercise = exercises.get(exercise_id)

    if not exercise:
        emit("output", "Ejercicio inválido\r\n")
        return

    sid = request.sid
    input_queue = queue.Queue()
    output_queue = queue.Queue()
    clients[sid] = {"input_queue": input_queue, "output_queue": output_queue}

    threading.Thread(
        target=run_exercise_with_graph,
        args=(exercise["func"], sid, input_queue, output_queue),
        daemon=True
    ).start()

    def streamer():
        while True:
            msg = output_queue.get()
            if msg is None:
                socketio.emit("end", room=sid)
                break
            if msg:
                socketio.emit("output", msg, room=sid)
    threading.Thread(target=streamer, daemon=True).start()


# ----------------------- Handlers Input -----------------------
@socketio.on("input")
def handle_input(data):
    sid = request.sid
    client = clients.get(sid)
    if not client:
        emit("output", "No hay ejercicio en ejecución.\r\n")
        return
    client["input_queue"].put(data.strip())
