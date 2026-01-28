from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    resultado = None
    
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        cantidad = request.form.get('cantidad')
        tarjeta_cineco = request.form.get('tarjeta_cineco')
        
        if not nombre:
            error = "Por favor escribe tu nombre"
        elif not cantidad or not cantidad.isdigit():
            error = "Por favor escribe cuántas boletas quieres"
        else:
            cantidad = int(cantidad)
            
            if cantidad > 7:
                error = "Máximo 7 boletas por persona"
            elif cantidad < 1:
                error = "Debes comprar al menos 1 boleta"
            else:
                precio_boleta = 12000
                subtotal = precio_boleta * cantidad
                
                if cantidad > 5:
                    descuento_cantidad = 0.15
                elif cantidad >= 3:
                    descuento_cantidad = 0.10
                else:
                    descuento_cantidad = 0.0
                
                monto_descuento = subtotal * descuento_cantidad
                total = subtotal - monto_descuento
                
                descuento_cineco = 0
                if tarjeta_cineco == 'on':
                    descuento_cineco = total * 0.10
                    total = total - descuento_cineco
                
                resultado = {
                    'nombre': nombre,
                    'cantidad': cantidad,
                    'precio_boleta': precio_boleta,
                    'subtotal': subtotal,
                    'descuento_cantidad': descuento_cantidad * 100,
                    'monto_descuento': monto_descuento,
                    'descuento_cineco': descuento_cineco,
                    'total': total,
                    'tiene_tarjeta': tarjeta_cineco == 'on'
                }
    
    return render_template('index.html', error=error, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
