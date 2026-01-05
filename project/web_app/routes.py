import importlib
import project.web_app.modules as modules
from flask import Blueprint, render_template, abort, g

main_bp = Blueprint('main', __name__)

# Inyección de components en todas las plantillas
@main_bp.before_app_request
def inject_components():
    key_value_lists = [{"id": module["id"], "module_name": module["module_name"]} for module in modules.information()]
    # Esto hará que 'components' esté disponible en todas las plantillas
    g.components = key_value_lists

#------------------------------------- HOME ----------------------------------------------
@main_bp.route('/')
def home():
    return render_template('00_home.html')

#------------------------------------- MODULE ----------------------------------------------
@main_bp.route('/module/<int:id_module>')
def module_page(id_module):
    modulo = next((m for m in modules.information() if m['id'] == id_module), None)

    if not modulo:
        abort(404)

    submenu = []
    if 'module_menu' in modulo:
        module_path, func_name = modulo['module_menu'].rsplit('.', 1)
        imported_module = importlib.import_module(module_path)
        submenu_func = getattr(imported_module, func_name)
        exercises = submenu_func()

        submenu = [{"id": idx + 1, "statement": exercise["statement"], "exercise": exercise["exercise"]}
                   for idx, exercise in enumerate(exercises)]

    return render_template('01_practice.html', modulo=modulo, submenu=submenu)

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