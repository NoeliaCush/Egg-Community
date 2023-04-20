package Entidad;

public class Animal {

    protected String nombre;
    protected Integer edad;
    protected boolean cola;

    public Animal(String nombre, Integer edad, boolean cola) {
        this.nombre = nombre;
        this.edad = edad;
        this.cola = cola;
    }

    public Animal() {
    }

    public void hacerRuido() {
        System.out.println("*Ruido de animal*");
    }

}
