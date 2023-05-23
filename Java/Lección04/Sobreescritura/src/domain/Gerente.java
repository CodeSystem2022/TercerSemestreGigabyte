
package domain;

public class Gerente extends Empleado{
    private String departamento;
    
    public Gerente(String nombre, Double sueldo, String departamento){
        super(nombre, sueldo);
        this.departamento = departamento;
                       
    }
    // sobrescribimos el método
    @Override
    
    public String ObtenerDetalles(){
        return super.ObtenerDetalles()+ ", departamento: " + this.departamento;
    }
    
    
}
