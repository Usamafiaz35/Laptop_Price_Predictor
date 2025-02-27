from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired

class LaptopForm(FlaskForm):
    company = SelectField('Brand', choices=[], validators=[DataRequired()])
    type = SelectField('Type', choices=[], validators=[DataRequired()])
    ram = SelectField('RAM (GB)', choices=[(str(i), str(i)) for i in [2,4,6,8,12,16,24,32,64]], validators=[DataRequired()])
    weight = FloatField('Weight of the Laptop', validators=[DataRequired()])
    touchscreen = SelectField('Touchscreen', choices=[('0', 'No'), ('1', 'Yes')], validators=[DataRequired()])
    ips = SelectField('IPS', choices=[('0', 'No'), ('1', 'Yes')], validators=[DataRequired()])
    screen_size = FloatField('Screen Size (in inches)', validators=[DataRequired()])
    resolution = SelectField('Screen Resolution', choices=[('1920x1080', '1920x1080'), ('1366x768', '1366x768'), ('1600x900', '1600x900'), ('3840x2160', '3840x2160')], validators=[DataRequired()])
    cpu = SelectField('CPU', choices=[], validators=[DataRequired()])
    hdd = SelectField('HDD (GB)', choices=[(str(i), str(i)) for i in [0,128,256,512,1024,2048]], validators=[DataRequired()])
    ssd = SelectField('SSD (GB)', choices=[(str(i), str(i)) for i in [0,128,256,512,1024]], validators=[DataRequired()])
    gpu = SelectField('GPU', choices=[], validators=[DataRequired()])
    os = SelectField('OS', choices=[], validators=[DataRequired()])
    
    submit = SubmitField('Predict Price')
