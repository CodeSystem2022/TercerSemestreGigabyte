public class Persona {

    //Atributos
    private int id;
    private String nombre;
    private String tel;
    private String email;
    private static int numeroPersonas=0;

    //Constructor

    public Persona(){
        this.id = ++Persona.numeroPersonas;
        //Este constructor vacio, cada vez que es llamado aumenta el contador en 1, en este caso id
    }

    //Constructor con Parametros          (Sobrecarga de constructores,ya que hay mas de un constructor)
    public Persona(String nombre, String tel, String email){
        this(); //Llamamos al constructor vacio. De esta manera tambien funciona el contador
        this.nombre = nombre;
        this.tel = tel;
        this.email = email;
    }



    //Metodos getter and setter
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


    //toString
    @Override
    public String toString() {
        return "Persona{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' +
                ", tel='" + tel + '\'' +
                ", email='" + email + '\'' +
                '}';
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan Perez","123123123","jperez@mail.com");
        System.out.println( persona1);
    }
}
