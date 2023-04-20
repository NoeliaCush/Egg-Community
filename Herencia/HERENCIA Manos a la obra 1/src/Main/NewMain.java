package Main;

import Entidad.Animal;
import Entidad.Gato;
import Entidad.Perro;
import java.util.ArrayList;

public class NewMain {

    public static void main(String[] args) {
    
        ArrayList<Animal> Animales = new ArrayList();
        
        Animal a = new Animal();
        Animal b = new Perro();
        Animal c = new Gato();
        
        Animales.add(a);
        Animales.add(b);
        Animales.add(c);
        
        for (Animal aux : Animales) {
            aux.hacerRuido();
        }
        
    }
    
}
