import flask
import csv
import os


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/cartaCredito", methods=["GET", "POST"])
def cartaCredito():
    if flask.request.method == "POST":    
        dbcsv = open("cartaCredito.csv", "a")
        row = csv.writer(dbcsv, delimiter=",")

        #variables
        Fecha =flask.request.form["Fecha"]
        Tipo =flask.request.form["Tipo"]
        NumeroIdentificacion =flask.request.form["NumeroIdentificacion"]
        Nombre =flask.request.form["Nombre"]
        Direccion =flask.request.form["Direccion"]
        Ciudad =flask.request.form["Ciudad"]
        Telefono =flask.request.form["Telefono"]
        Fax =flask.request.form["Fax"]
        CodigoCIIU =flask.request.form["CodigoCIIU"]
        ActividadEconomica =flask.request.form["ActividadEconomica"]
        TipoCuenta =flask.request.form["TipoCuenta"]
        NumCuenta =flask.request.form["NumCuenta"]
        NRegImportaVig =flask.request.form["NRegImportaVig"]
        Exento =flask.request.form["Exento"]
        EnDolaresAme =flask.request.form["EnDolaresAme"]
        Plazo =flask.request.form["Plazo"]
        ApartirDocTrans =flask.request.form["ApartirDocTrans"]
        Otro =flask.request.form["Otro"]
        Nombre1 =flask.request.form["Nombre1"]
        Direccion1 =flask.request.form["Direccion1"]
        Ciudad1 =flask.request.form["Ciudad1"]
        Telefono1 =flask.request.form["Telefono1"]
        Fax1 =flask.request.form["Fax1"]
        pais =flask.request.form["pais"]
        Vigencia =flask.request.form["Vigencia"]
        CodMoneda =flask.request.form["CodMoneda"]
        Monto =flask.request.form["Monto"]
        Tolerancia =flask.request.form["Tolerancia"]
        Otro1 =flask.request.form["Otro1"]
        UtilPago =flask.request.form["UtilPago"]
        ApartirDocTrans1 =flask.request.form["ApartirDocTrans1"]
        OtroDoc =flask.request.form["OtroDoc"]
        Dias =flask.request.form["Dias"]
        ECDSUPPDOMDLC =flask.request.form["ECDSUPPDOMDLC"]
        EmbarqueParciales =flask.request.form["EmbarqueParciales"]
        Transbordos =flask.request.form["Transbordos"]
        LugarEmbarque =flask.request.form["LugarEmbarque"]
        Fecha1 =flask.request.form["Fecha1"]
        LugarDestino =flask.request.form["LugarDestino"]
        DescrBrebeMerca =flask.request.form["DescrBrebeMerca"]
        PrescioMercaInco2000 =flask.request.form["PrescioMercaInco2000"]
        Tolerancia1 =flask.request.form["Tolerancia1"]
        Otro3 =flask.request.form["Otro3"]
        BancoNotifica =flask.request.form["BancoNotifica"]
        CodSwift =flask.request.form["CodSwift"]
        GasFueraColoCuenta =flask.request.form["GasFueraColoCuenta"]
        InstiNotifica =flask.request.form["InstiNotifica"]
        OriginalCopia =flask.request.form["OriginalCopia"]
        OriginalCopia1 =flask.request.form["OriginalCopia1"]
        ConociEmbarqueLimpio =flask.request.form["ConociEmbarqueLimpio"]
        ConsignadoOrdende =flask.request.form["ConsignadoOrdende"]
        Notificadoa =flask.request.form["Notificadoa"]
        SeñalandoFletes =flask.request.form["SeñalandoFletes"]
        OriginalCopia2 =flask.request.form["OriginalCopia2"]
        OriginalCopia3 =flask.request.form["OriginalCopia3"]
        OriginalCopia4 =flask.request.form["OriginalCopia4"]
        caratAreaRemiDoc =flask.request.form["caratAreaRemiDoc"]
        Dirigidoa =flask.request.form["Dirigidoa"]
        OriginalCopia5 =flask.request.form["OriginalCopia5"]
        OriginalCopia6 =flask.request.form["OriginalCopia6"]
        otro4 =flask.request.form["otro4"]
        OriginalCopia7 =flask.request.form["OriginalCopia7"]
        otro5 =flask.request.form["otro5"]
        CondAdicionales =flask.request.form["CondAdicionales"]

                             
        row.writerow([Fecha,Tipo,NumeroIdentificacion,Nombre,Direccion,Ciudad,Telefono,Fax,CodigoCIIU,ActividadEconomica,TipoCuenta,NumCuenta,NRegImportaVig,Exento,EnDolaresAme,Plazo,ApartirDocTrans,Otro,Nombre1,Direccion1,Ciudad1,Telefono1,Fax1,pais,Vigencia,CodMoneda,Monto,Tolerancia,Otro1,UtilPago,ApartirDocTrans1,OtroDoc,Dias,ECDSUPPDOMDLC,EmbarqueParciales,Transbordos,LugarEmbarque,Fecha1,LugarDestino,DescrBrebeMerca,PrescioMercaInco2000,Tolerancia1,Otro3,BancoNotifica,CodSwift,GasFueraColoCuenta,InstiNotifica,OriginalCopia,OriginalCopia1,ConociEmbarqueLimpio,ConsignadoOrdende,SeñalandoFletes,OriginalCopia2,OriginalCopia3,OriginalCopia4,caratAreaRemiDoc,Dirigidoa,OriginalCopia5,OriginalCopia6,otro4,OriginalCopia7,otro5,CondAdicionales])
        dbcsv.close()
        return "sus datos se guardaron con exito"
    else:
        return "este es el error que salta"


# ejecucion
if __name__ == ("__main__"):
    app.run(debug=True, host="0.0.0.0", port=5001)
