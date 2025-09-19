import flask
import csv
import os

# definir variables
app = flask.Flask(__name__)

# procesos
@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/importaciones", methods=["GET", "POST"])
def importaciones():
    if flask.request.method == "POST":    
        dbcsv = open("importaciones.csv", "a")
        row = csv.writer(dbcsv, delimiter=",")
        #variables

        numFormulario = flask.request.form["numFormulario"]
        importador = flask.request.form["importador"]
        numDocumentoImportador = flask.request.form["numDocumentoImportador"]
        nombreRepresentanteImportador = flask.request.form["nombreRepresentanteImportador"]
        direccionImportador = flask.request.form["direccionImportador"]
        telefonoImportador = flask.request.form["telefonoImportador"]
        ciudadImportador = flask.request.form["ciudadImportador"]
        direccionEntidad = flask.request.form["direccionEntidad"]
        telefonoEntidad = flask.request.form["telefonoEntidad"]
        ciudadEntidad = flask.request.form["ciudadEntidad"]
        agencia = flask.request.form["agencia"]
        numDocumentoAgencia = flask.request.form["numDocumentoAgencia"]
        telefonoAgencia = flask.request.form["telefonoAgencia"]
        ciudadAgencia = flask.request.form["ciudadAgencia"]
        direccionTerritorial = flask.request.form["direccionTerritorial"]
        claseSolicitud = flask.request.form["claseSolicitud"]
        Anexos = flask.request.form["Anexos"]
        actividadImportador = flask.request.form["actividadImportador"]
        claseImportador = flask.request.form["claseImportador"]
        regimen = flask.request.form["regimen"]
        cupos = flask.request.form["cupos"]
        estadoMercancia = flask.request.form["estadoMercancia"]
        exportador = flask.request.form["exportador"]
        ciudadExportador = flask.request.form["ciudadExportador"]
        consignatorio = flask.request.form["consignatorio"]
        aduana = flask.request.form["aduana"]
        paisOrigen = flask.request.form["paisOrigen"]
        paisCompra = flask.request.form["paisCompra"]
        puertoEmbarque = flask.request.form["puertoEmbarque"]
        via = flask.request.form["via"]
        condicionesReembolso = flask.request.form["condicionesReembolso"]
        noReembolsables = flask.request.form["noReembolsables"]
        reembolsableDig = flask.request.form["reembolsableDig"]
        tiempoReembolso = flask.request.form["tiempoReembolso"]
        monedaNegociacion = flask.request.form["monedaNegociacion"]
        tasaCambioUs = flask.request.form["tasaCambioUs"]
        valorTotalMoneda = flask.request.form["valorTotalMoneda"]
        valorTotalDolares = flask.request.form["valorTotalDolares"]
        valorTotalDolaresLetra = flask.request.form["valorTotalDolaresLetra"]
        solicitudesEspeciales = flask.request.form["solicitudesEspeciales"]
        solicitarVistoBueno = flask.request.form["solicitarVistoBueno"]
        referenciaVistoBueno = flask.request.form["referenciaVistoBueno"]
        anexosVistoBueno = flask.request.form["anexosVistoBueno"]
        numSubpartida = flask.request.form["numSubpartida"]
        posicionArancelaria = flask.request.form["posicionArancelaria"]
        E = flask.request.form["E"]
        unidadComercial = flask.request.form["unidadComercial"]
        C = flask.request.form["C"]
        cantidad = flask.request.form["cantidad"]
        precioUnitario = flask.request.form["precioUnitario"]
        valorTotal = flask.request.form["valorTotal"]
        descripcionMercancia = flask.request.form["descripcionMercancia"]
        numItems = flask.request.form["numItems"]
        unidadComercialItems = flask.request.form["unidadComercialItems"]
        cItems = flask.request.form["cItems"]
        cantidadItems = flask.request.form["cantidadItems"]
        precioUnitarioItems = flask.request.form["precioUnitarioItems"]
        valorTotalItems = flask.request.form["valorTotalItems"]
        numItems1 = flask.request.form["numItems1"]
        unidadComercialItems1 = flask.request.form["unidadComercialItems1"]
        cItems1 = flask.request.form["cItems1"]
        cantidadItems1 = flask.request.form["cantidadItems1"]
        precioUnitarioItems1 = flask.request.form["precioUnitarioItems1"]
        valorTotalItems1 = flask.request.form["valorTotalItems1"]
        numGasto = flask.request.form["numGasto"]
        valorTotalGastos = flask.request.form["valorTotalGastos"]
        descripcionGasto = flask.request.form["descripcionGasto"]
        numDescuento = flask.request.form["numDescuento"]
        valorTotalDescuento = flask.request.form["valorTotalDescuento"]
        descripcionDescuento = flask.request.form["descripcionDescuento"]
        
        row.writerow([numFormulario,importador,numDocumentoImportador,nombreRepresentanteImportador,direccionImportador,telefonoImportador,ciudadImportador,direccionEntidad,telefonoEntidad,ciudadEntidad,agencia,numDocumentoAgencia,telefonoAgencia,ciudadAgencia,direccionTerritorial,claseSolicitud,Anexos,actividadImportador,claseImportador,regimen,cupos,estadoMercancia,exportador,ciudadExportador,consignatorio,aduana,paisOrigen,paisCompra,puertoEmbarque,via,condicionesReembolso,noReembolsables,reembolsableDig,tiempoReembolso,monedaNegociacion,tasaCambioUs,valorTotalMoneda,valorTotalDolares,valorTotalDolaresLetra,solicitudesEspeciales,solicitarVistoBueno,referenciaVistoBueno,anexosVistoBueno,numSubpartida,posicionArancelaria,E,unidadComercial,C,cantidad,precioUnitario,valorTotal,descripcionMercancia,numItems,unidadComercialItems,cItems,cantidadItems,precioUnitarioItems,valorTotalItems,numItems1,unidadComercialItems1,cItems1,cantidadItems1,precioUnitarioItems1,valorTotalItems1,numGasto,valorTotalGastos,descripcionGasto,numDescuento,valorTotalDescuento,descripcionDescuento,])
        dbcsv.close()
        return "sus datos se guardaron con exito"
    else:
        return "error"
# ejecucion
if __name__ == ("__main__"):
    app.run(debug=True, host="0.0.0.0")