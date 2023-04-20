package newpackage;

import Entidades.Perro;
import Entidades.Gato;
import Entidades.Caballo;
import Entidades.Animal;


public class MAIN {

    public static void main(String[] args) {
        
        //Declaración del objeto Perro
        Animal perro1 = new Perro("Atenea", "Croquetas", 1, "Golden");
        perro1.Alimentarse();
        
        //Declaración del objeto Perro
        Animal perro2 = new Perro("Teddy", "Croquetas", 10, "Chihuahua");
        perro2.Alimentarse();
        
        //Declaración del objeto Gato
        Animal gato1 = new Gato("Liv", "Atun", 7, "Rayas");
        gato1.Alimentarse();
        
        //Declaración del objeto Caballo
        Animal caballo1 = new Caballo("Spark", "Pasto", 25, "Fino");
        caballo1.Alimentarse();
        
        
        
    }
    
}
