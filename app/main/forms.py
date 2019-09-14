from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    pitch = TextAreaField('Your Pitch', validators=[Required()])
    # my_category = StringField('Category', validators=[Required()])
    my_category = SelectField('Category', choices=[('Interview-Pitch','Interview Pitch'),('Product-Pitch','Product Pitch'),('Promotion-Pitch','Promotion Pitch'),('Business','Business'),('Academic','Academic'),('Political','Political'),('Technology','Technology'),('Health','Health')],validators=[Required()])
    submit = SubmitField('Pitch!')

