from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#LOGIN MÉDICO
class LoginForm(FlaskForm):
    crm = StringField('CRM', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar de Mim')
    submit = SubmitField('Login')

#CADASTRO E LOGIN DE PACIENTE

class Form1(FlaskForm):
    username = StringField('Usuário',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    cpf = StringField('CPF',
                        validators=[DataRequired(), Length(min=9, max=11)])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Confirme a Senha',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Concluir Cadastro')


class Form2(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    cpf = StringField('CPF', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar de Mim')
    submit = SubmitField('Login')

