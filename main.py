
from flask import Flask, request,render_template
import forms
app=Flask(__name__)


@app.route("/")
def calculo():
    return render_template("formulario.html", result=None)

@app.route("/resultado", methods=["GET", "POST"])
def multiplica():
    if request.method == "POST":
        num1 = float(request.form.get("n1"))
        num2 = float(request.form.get("n2"))
        oper = request.form.get("operacion")

        result = None

        if oper == 'suma':
            result = num1 + num2
        elif oper == 'resta':
            result = num1 - num2
        elif oper == 'multiplicacion':
            result = num1 * num2
        elif oper == 'division':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "no es divisible entre 0"

        return render_template('formulario.html', result=result)

    return render_template('formulario.html', result=None)

@app.route('/DistanciaDosPuntos', methods=['GET', 'POST'])
def d2p():
    d = None

    if request.method == 'POST':
        x1 = float(request.form['x1'])
        y1 = float(request.form['y1'])
        x2 = float(request.form['x2'])
        y2 = float(request.form['y2'])
        d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return render_template('formDistance.html', distance=d)


@app.route("/resistencias", methods=['GET', 'POST'])
def calResistencia():
    resistencia_form = resistencia.ResistenciaForm(request.form)

    if request.method == 'POST':
        colors = obtenerColores()
        
        codigo_colores = {
          colors[0]: 0,
          colors[1]: 1,
          colors[2]: 2,
          colors[3]: 3,
          colors[4]: 4,
          colors[5]: 5,
          colors[6]: 6,
          colors[7]: 7,
          colors[8]: 8,
          colors[9]: 9,
          colors[10]: 0.05,
          colors[11]: 0.1
        }

        color1 = resistencia_form.bandaUno.data
        color2 = resistencia_form.bandaDos.data
        color3 = resistencia_form.bandaTres.data
        color4 = request.form.get('tolerance')

        bandaUno = codigo_colores[color1]
        bandaDos = codigo_colores[color2]
        bandaTres = codigo_colores[color3]
        tolerancia = codigo_colores[color4]

        valorNominal = (bandaUno * 10 + bandaDos) * 10 ** bandaTres
        
        minimo = 0
        maximo = 0
        if tolerancia == 0.05:
            maximo = valorNominal + valorNominal*(0.05)
            minimo = valorNominal - valorNominal*(0.05)
        elif tolerancia == 0.1:
            maximo = valorNominal + valorNominal*(0.1)
            minimo = valorNominal - valorNominal*(0.1)

        return render_template('resistencias.html', form = resistencia_form, color1 = color1, color2 = color2, color3 = color3, color4 = color4, 
                               valorNominal = valorNominal, minimo =  minimo, maximo = maximo)
    
    return render_template('resistencias.html', form = resistencia_form)

def obtenerColores():
    lista = ["black", "brown", "red", "orange", 
             "yellow", "green", "blue", "violet", "gray", 
             "white", "gold", "silver"]
    return lista


if __name__ == "__main__":
    app.run(debug=True)
