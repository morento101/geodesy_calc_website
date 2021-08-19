from flask import Blueprint, render_template, request
from flask.helpers import flash
from flask_login import login_required, current_user
import website.calculating as f

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    print(current_user)
    return render_template("calculate.html", user=current_user)


@views.route("/calc_zone", methods=["GET", "POST"])
@login_required
def calc_zone():
    res = ''
    if request.method == 'POST':
        zone = request.form.get('zoneNumber')
        distance = request.form.get('distance')
        direction = request.form.get('direction')
        if zone:
            if distance:
                if direction:
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
                else:
                    flash("Введіть напрям", category="error")
            else:
                flash("Введіть відстань", category="error")
        else:
            flash("Введіть номер зони", category="error")
    return render_template('calc/zone.html', user=current_user, res=res)


@views.route('/calc_map_accuracy', methods=["GET", "POST"])
@login_required
def calc_map_accuracy():
    res = ''
    if request.method == "POST":
        scale = request.form.get('scale')
        if scale:
            try:
                scale = scale.replace(' ', '')
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
    return render_template('calc/map_accuracy.html', user=current_user, res=res)


@views.route('/calc_segmentation', methods=["GET", "POST"])
@login_required
def calc_segmentation():
    res=''
    if request.method == 'POST':
        segment = request.form.get('segment')
        try:
            scale = f.get_scale_from_segment(segment)
        except Exception as e:
            flash(f'{e}', category='error')
        else:
            res = scale
    return render_template('calc/segmentation.html', user=current_user, res=res)


@views.route('/calc_dividing', methods=["GET", "POST"])
@login_required
def calc_dividing():
    res = ''
    if request.method == "POST":
        dividing_scale = request.form.get('dividing1')
        divider_scale = request.form.get('dividing2')
        if dividing_scale:
            if divider_scale:
                try:
                    res = f.divide_scales(dividing_scale, divider_scale)
                except Exception as e:
                    flash(f"{e}", category="error")
            else:
                flash('Введіть Масштаб Трапеції, Що Потрібно Отримати В Результаті Ділення', category="error")
        else:
            flash('Введіть Масштаб Трапеції, Що Ділиться', category="error")
    return render_template('calc/dividing.html', user=current_user, res=res)


@views.route('/calc_size', methods=["GET", "POST"])
@login_required
def calc_size():
    res = ''
    return render_template('calc/size.html', user=current_user, res=res)
