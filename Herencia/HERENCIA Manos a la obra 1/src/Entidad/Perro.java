package Entidad;

public class Perro extends Animal {

    public Perro(String nombre, Integer edad, boolean cola) {
        super(nombre, edad, cola);
    }

    public Perro() {
      
    }

    @Override
    public void hacerRuido() {
        System.out.println("El perro hace: ¡GUAU!");
    }
    
        
}
