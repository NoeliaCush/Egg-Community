package MAIN.ENTIDADES;

import MAIN.INTERFACES.Accion;

public class Animal implements Accion {

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

    @Override
    public void pasear(int cantVueltas) {
        System.out.println("El animal ha dado " + cantVueltas + " vueltas");
    }

    @Override
    public void comerAlimento(int cantidad) {
        System.out.println("El animal ha comido " + cantidad + " veces");
    }

    
    
}
