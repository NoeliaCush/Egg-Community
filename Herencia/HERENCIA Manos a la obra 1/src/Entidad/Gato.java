package Entidad;

public class Gato extends Animal {

    public Gato(String nombre, Integer edad, boolean cola) {
        super(nombre, edad, cola);
    }

    public Gato() {
       
    }

    @Override
    public void hacerRuido() {
        System.out.println("El gato hace: ¡MIAU!");
    }
    
        
}
