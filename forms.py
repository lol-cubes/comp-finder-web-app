from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class InputFileForm(FlaskForm):
    states = TextAreaField('States', validators=[DataRequired(), Length(min=4, max=471)], render_kw={'rows': '10', 'cols': '50'})
    address = StringField('Address or Coordinates', validators=[DataRequired()])
    submit = SubmitField('Find Competitions Near You')