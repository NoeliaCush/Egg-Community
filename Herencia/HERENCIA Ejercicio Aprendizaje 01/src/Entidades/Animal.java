package Entidades;


/**
 * Tenemos una clase padre Animal
 * Tendrá como atributos el nombre, alimento, edad y raza del Animal.
 * Crear un método en la clase Animal deberá mostrar luego un
 * mensaje por pantalla informando de que se alimenta
 */
public class Animal {

    //Atributos CLASE MADRE
    protected String nombre;
    protected String alimento;
    protected int edad;
    protected String razaAnimal;

    //Constructor por parámetro
    public Animal(String nombre, String alimento, int edad, String razaAnimal) {
        this.nombre = nombre;
        this.alimento = alimento;
        this.edad = edad;
        this.razaAnimal = razaAnimal;
    }

   //El M{etodo
    public void Alimentarse() {
        System.out.println("El animal se alimenta de:");
    }
}
