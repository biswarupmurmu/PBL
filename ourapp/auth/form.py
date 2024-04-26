from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import Email, EqualTo, InputRequired, length


class SignupForm(FlaskForm):
    fname = StringField("First name", validators=[InputRequired()])
    lname = StringField("Last name")
    email = EmailField("Email", validators=[InputRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            length(min=4, max=20),
        ],
        
    )
    confirm_password = PasswordField(
        "Confirm password",
        validators=[
            InputRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    
    def process_data(self):
        self.fname.data = self.fname.data.strip()
        self.lname.data = self.lname.data.strip()
        self.email.data = self.email.data.strip().lower()

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired()])

        
