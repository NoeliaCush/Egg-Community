/**
 * Vamos a crear una interfaz con un método abstracto. Luego desde el main intentaremos instanciar
 * un objeto a partir de la interfaz
 */

package MAIN;

import MAIN.ENTIDADES.Animal;

public class NewMain {

    public static void main(String[] args) {
    
      Animal a1 = new Animal();
      
      a1.pasear(4);
      a1.comerAlimento(2);
      a1.metodo();
        
        
    }
    
}
