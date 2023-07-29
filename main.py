from flask import Flask,request,render_template,jsonify

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def quadratic_eq():
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        delta = (b**2) - 4*a*c
        
        if delta <0:
            result = f"The quadratic equation : {a}*x^2 + {b}*x + {c} has no real roots."
            
        elif delta == 0:
            x = (-b)/(2*a)
            result = f"The quadratic equation : {a}*x^2 + {b}*x + {c} has one real root: {str(x)}"
        else:
            x1 = (-b + delta**(1/2)) / (2*a)
            x2 = (-b - delta**(1/2)) / (2*a)
            result = f"The quadratic equation {a}*x^2 + {b}*x + {c} has two real roots: {str(x1)} and {str(x2)}"
        return render_template("quadratic.html", result = result)
    else:
        return render_template("quadratic.html")
    
    
    
@app.route('/quadratic_postman',methods=['POST'])
def quadratic_solver_postman():
    if request.method == 'POST':
        a = float(request.json['a'])
        b = float(request.json['b'])
        c = float(request.json['c'])
        delta = (b**2) - 4*a*c
        if delta < 0:
            result = f"The quadratic equation : {a}*x^2 + {b}*x + {c} has no real roots."
        elif delta == 0:
            x = (-b) / (2*a)
            result = f"The quadratic equation : {a}*x^2 + {b}*x + {c} has one real root: {str(x)}"
        else:
            x1 = (-b + delta**(1/2)) / (2*a)
            x2 = (-b - delta**(1/2)) / (2*a)
            result = f"The quadratic equation {a}*x^2 + {b}*x + {c} has two real roots: {str(x1)} and {str(x2)}"
        
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)