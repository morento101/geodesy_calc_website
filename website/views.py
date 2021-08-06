from flask import Blueprint, render_template, request
from flask.helpers import flash
from flask_login import login_required, current_user
import website.calc_func_py.functions_for_calc as f

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("calculate.html", user=current_user)

@views.route("/calc_zone", methods=["GET", "POST"])
@login_required
def calc_zone():
    if request.method == 'POST':
        zone = request.form.get('zoneNumber')
        distance = request.form.get('distance')
        direction = request.form.get('direction')
        if zone:
            if distance:
                if direction:
                    res = ''
                    try:
                        zone = int(zone)
                    except Exception:
                        flash("Зона повинна бути цілим додатнім числом", category='error')
                    else:
                        try:
                            distance = float(distance)
                        except Exception:
                            flash('Відстань може бути лише цілим або дробовим додатнім числом', category='error')
                        else:
                            try:
                                res = f.y_value_for_zones(zone, distance, direction)
                            except Exception as e:
                                flash(f'{e}', category="error")
                    finally:
                        return render_template("calc_zone.html", user=current_user, res=res)
                else:
                    flash("Введіть напрям", category="error")
            else:
                flash("Введіть відстань", category="error")
        else:
            flash("Введіть номер зони", category="error")
        return render_template("calc_zone.html", user=current_user)
    else:
        return render_template("calc_zone.html", user=current_user)


@views.route('/calc_map_accuracy', methods=["GET", "POST"])
@login_required
def calc_map_accuracy():
    if request.method == "POST":
        scale = request.form.get('scale')
        if scale:
            try:
                scale = int(scale)
            except Exception as e:
                flash('Масштаб повинен бути цілим додатнім числом', category="error") 
            else:
                try:
                    res = f.accuracy_of_scale(scale)
                except Exception as e:
                    flash(f"{e}", category="error")
        else:
            flash('Введіть масштаб', category="error")
    return render_template('calc_map_accuracy.html', user=current_user)