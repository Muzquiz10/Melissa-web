from flask import Flask, render_template, redirect, url_for
from forms import PresupuestoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una-clave-super-secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trabajos')
def trabajos():
    return render_template('trabajos.html')

@app.route('/precios')
def precios():
    return render_template('precios.html')

@app.route('/nosotros')
def sobre_nosotros():
    return render_template('sobre_nosotros.html')

@app.route('/presupuesto', methods=['GET', 'POST'])
def presupuesto():
    form = PresupuestoForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('presupuesto.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
