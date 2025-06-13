from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class PresupuestoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[Email()])
    tipo_evento = SelectField('Tipo de evento', choices=[('boda', 'Boda'), ('cumpleaños', 'Cumpleaños'), ('otro', 'Otro evento')])
    detalles = TextAreaField('Cuéntanos los detalles', validators=[DataRequired()])
    submit = SubmitField('Enviar solicitud')
