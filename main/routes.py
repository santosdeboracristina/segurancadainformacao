from flask import render_template, url_for, flash, redirect
from main import app
from main.forms import LoginForm, Form1, Form2
from main.models import Paciente, Prontuario

prontuarios = [
    {
        'medico': 'Corey Schafer',
        'titulo': 'Prontuario 1',
        'conteudo': 'Nome do pdf1',
        'data_postagem': 'April 20, 2018'
    },
    {
        'medico': 'Debora Santos',
        'titulo': 'Prontuario 2',
        'conteudo': 'Nome do pdf2',
        'data_postagem': 'April 20, 2018'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', prontuarios=prontuarios)


@app.route("/login-medico", methods=['GET', 'POST'])
def login_doutor():
    form = LoginForm()
    if form.validate_on_submit():
        if form.crm.data == '123456' and form.password.data == 'medico':
            flash('Você está logado!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Falha ao conectar, por favor, verifique suas credenciais!', 'danger')
    return render_template('login.html', title='Login', form=form)


#ROTAS PARA O PACIENTE

@app.route("/registro-paciente", methods=['GET', 'POST'])
def register_paciente():
    form1 = Form1()
    if form1.validate_on_submit():
        flash(f'Conta Criada para {form1.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register-paciente.html', title='Cadastre-se', form=form1)


@app.route("/login-paciente", methods=['GET', 'POST'])
def login_paciente():
    form2 = Form2()
    if form2.validate_on_submit():
        if form2.email.data == 'paciente@blog.com' and form2.password.data == '1234':
            flash('Você está logado!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Falha ao conectar, por favor, verifique suas credenciais!', 'danger')
    return render_template('login-paciente.html', title='Login', form=form2)
