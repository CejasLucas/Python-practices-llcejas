import importlib
import project.web_app.modules as modules
from flask import Blueprint, render_template, abort

main_bp = Blueprint('main', __name__)

#------------------------------------- HOME ----------------------------------------------
@main_bp.route('/')
def main_menu():
    key_value_lists = []
    for module in modules.information():
        key_value_lists.append({"id": module["id"], "module_name": module["module_name"]})
    return render_template('00_home.html', components=key_value_lists)


#------------------------------------- MODULE ----------------------------------------------
@main_bp.route('/module/<file_name>')
def module_page(file_name):
    modulo = next((m for m in modules.information() if m['file_name'] == file_name), None)
    if not modulo: abort(404)

    submenu = []
    if 'submenu_func' in modulo:
        module_path, func_name = modulo['submenu_func'].rsplit('.', 1)
        imported_module = importlib.import_module(module_path)
        submenu_func = getattr(imported_module, func_name)
        exercises = submenu_func()
        submenu = [{"id": int(k), "name": v["name"]} for k,v in exercises.items()]

    return render_template('python_basic.html', modulo=modulo, submenu=submenu)


#------------------------------------- EXERCISE ----------------------------------------------
@main_bp.route('/module/<file_name>/exercise/<int:exercise_id>')
def run_exercise(file_name, exercise_id):
    modulo = next((m for m in modules.information() if m['file_name'] == file_name), None)
    if not modulo or 'submenu_func' not in modulo: abort(404)

    return render_template(
        'task.html',
        file_name=file_name,
        exercise_id=exercise_id,
        modulo=modulo
    )

#------------------------------------- GRAPHIC ----------------------------------------------
@main_bp.route('/graphic')
def graphics():
    return render_template('graphic.html')