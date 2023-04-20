
package MAIN.INTERFACES;

public interface Accion {
    
    public void pasear(int cantVueltas);
    public void comerAlimento (int cantidad);
    
    default void metodo(){
        System.out.println("hola");
    }
}
