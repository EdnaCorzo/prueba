from flask import Flask, request, render_template, jsonify
import os
import db

app= Flask(__name__)
app.secret_key= os.urandom(32)

@app.route('/id')
def consultaId():
    return render_template('consultaproducto.html')

@app.route('/listProduct', methods=['GET'])
def listProductById():
    idp = request.args.get('idproducto')
    #output= db.getProductoSecure(idp)
    output= db.getProducto(idp)
    return render_template("productos.html", productos=output)


if __name__=="__main__":
    app.run(debug=True)