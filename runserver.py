from flask import Flask, render_template, request, redirect, session
import random 	     

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # asignar una clave secreta por motivos de seguridad 


@app.route('/')
def show():
    
    return render_template("index.html")

@app.route('/random',methods=['POST'] )
def random_num():
    session['num_random']= random.randint(1, 100) 		# random number between 1-1
    session['mensaje1']= "Se a generado el numero. suerte"
    return redirect("/play")

@app.route('/play')
def play():
    mensaje="Ingresa un numero "
    return render_template("index.html",mensaje_form=mensaje)

@app.route('/adivinar',methods=['POST'])
def play2():
    num_adi=request.form['num_adivinador']
    print("********* num_adi :",num_adi)
    if session['num_random']== int(num_adi):
        session['mensaje2']="Ganaste !!!!!!!! presiona de nuevo el boton para empesar otro juego "
        session['color'] = 'green'
    if session['num_random']> int(num_adi):
        session['mensaje2']="Intenta con un numero mas grande "
        session['color'] = 'red'
    if session['num_random']< int(num_adi):
        session['mensaje2']="Intenta con un numero mas chico "
        session['color'] = 'red'
    
    #return render_template("index.html",mensaje_form=mensaje)
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    