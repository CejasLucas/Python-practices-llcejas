import importlib
from flask import Blueprint, render_template, abort, g
import project.web_app.modules as modules

main_bp = Blueprint("main", __name__)

@main_bp.before_app_request
def inject_components():
    g.components = [
        {"id": m["id"], "module_name": m["module_name"]}
        for m in modules.information()
    ]


@main_bp.route("/")
def home():
    return render_template("00_home.html")


@main_bp.route("/module/<int:id_module>")
def module_page(id_module):
    modulo = next((m for m in modules.information() if m["id"] == id_module), None)
    if not modulo:
        abort(404)

    module_path, func_name = modulo["module_menu"].rsplit(".", 1)
    imported_module = importlib.import_module(module_path)
    submenu_func = getattr(imported_module, func_name)

    exercises = submenu_func()
    submenu = [
        {"id": i + 1, "statement": ex["statement"]}
        for i, ex in enumerate(exercises)
    ]

    return render_template("01_practice.html", modulo=modulo, submenu=submenu)


@main_bp.route("/module/<folder_name>/exercise/<int:exercise_id>")
def run_exercise(folder_name, exercise_id):
    modulo = next((m for m in modules.information() if m["folder_name"] == folder_name), None)
    if not modulo:
        abort(404)

    module_path, func_name = modulo["module_menu"].rsplit(".", 1)
    imported_module = importlib.import_module(module_path)
    submenu_func = getattr(imported_module, func_name)
    exercises = submenu_func()

    if exercise_id < 1 or exercise_id > len(exercises):
        abort(404)

    return render_template(
        "02_task.html",
        folder_name=folder_name,
        exercise_id=exercise_id,
        modulo=modulo,
        statement=exercises[exercise_id - 1]["statement"]
    )



@main_bp.route('/graphic')
def graphics():
    return render_template('03_graphic.html')