class Cliente extends Persona {

    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fecharegistro) {
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = fechaRegistro;
    }
    get idCliente() {
        return this._idCliente;
    }
    get fecharegistro() {
        return this._fechaRegistro = fecharegistro;
    }
    set fecharegitro(fecharegistro) {
        this._fechaRegistro = fechaRegistro;
    }
    toString() {
        return `
        ${super.toString()} 
        ${this._idCliente} 
        ${this._fecharegistro}`;
    }
}
