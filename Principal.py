from flask import render_template, request
from Main import app, db, Departamento, Ferias


@app.route("/pagina_relatorio", methods=["GET", "POST"])
def pagina_gera_relatorio():
    if request.method == "POST":
        departamento_id = request.form.get("departamento")

        if departamento_id:
            ferias = db.session.query(Ferias, Departamento).join(Departamento).filter(Departamento.id == departamento_id).all()
        else:
            ferias = db.session.query(Ferias, Departamento).join(Departamento).all()

        departamentos = Departamento.query.all()

        return render_template('pagina_relatorio.html', ferias=ferias, departamentos=departamentos)

    ferias = db.session.query(Ferias, Departamento).join(Departamento).all()
    departamentos = Departamento.query.all()

    return render_template('pagina_relatorio.html', ferias=ferias, departamentos=departamentos)
