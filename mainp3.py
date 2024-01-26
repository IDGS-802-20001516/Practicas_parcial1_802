from flask import Flask, request,render_template
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

if __name__ == "__main__":
    app.run(debug=True)