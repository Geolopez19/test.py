from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración para enviar correos electrónicos
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'geovannysamuel97@gmail.com'
app.config['MAIL_PASSWORD'] = 'msto vjgx ghdd qlby'

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        msg = Message(subject='Nuevo mensaje de contacto',
                      sender='geovannysamuel97@gmail.com',
                      recipients=['geovannysamuel97@gmail.com'])
        msg.body = f"Nombre: {name}\nEmail: {email}\nMensaje: {message}"
        mail.send(msg)
        
        # Redireccionar a la página de confirmación
        return redirect(url_for('sms'))
    return render_template('index.html')

@app.route('/sms')
def sms():
    return render_template('sms.html')

if __name__ == '__main__':
    app.run(debug=True)
