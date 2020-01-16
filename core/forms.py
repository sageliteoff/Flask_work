from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField,
                    RadioField, DateField, IntegerField, SelectField)
from wtforms.validators import DataRequired, Email

class SignUpForm(FlaskForm):
    firstname = StringField(
                "First name",
                validators=[DataRequired()],
                render_kw={"class": "form-control form-input-style",})
    lastname = StringField(
                "Last name",
                validators=[DataRequired()],
                render_kw={"class": "form-control form-input-style",})
    birthday = StringField(
                "Birthday",
                validators = [DataRequired()],
                render_kw = { "id" : "bday", "class" : "form-control form-input-style" })
    gender = RadioField(
                    "Gender",
                    validators = [DataRequired()],
                    choices=[
                        ("Male", "Male"),
                        ("Female", "Female")])
    email = StringField(
                "Email",
                validators = [DataRequired(), Email()],
                render_kw = {"class" : "form-control form-input-style" })
    phonenumber = IntegerField(
                "Phone Number",
                validators = [DataRequired()],
                render_kw = {"class" : "form-control form-input-style" })
    subject = SelectField(
                "Subject",
                validators = [DataRequired()],
                choices = [
                    ("default", "Choose a Subject"),
                    ("subject 1", "subject 1"),
                    ("subject 2", "subject 2")],
                    render_kw = {"class" : "form-control form-input-style" })
    submit = SubmitField("Submit", render_kw = {"class" : "btn btn-primary px-5" })


class SearchBarForm(FlaskForm):
    searchbar = StringField("Search", validators=[DataRequired("This Field is required")])
    submit = SubmitField("Search")