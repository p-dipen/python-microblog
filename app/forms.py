from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
import email_validator

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


class SendForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    text_body = TextAreaField('Message', validators=[DataRequired()])
    from_email = StringField('From email', validators=[DataRequired(), Email(granular_message=True)])
    recipients_email = StringField('Add recipients', validators=[DataRequired(), Email(granular_message=True)])
    submit = SubmitField('Send Email')