/**
 * Finalmente, en el main debemos realizar lo siguiente:
 * Vamos a crear una Lavadora y un Televisor y llamar a los métodos necesarios para mostrar
 * el precio final de los dos electrodomésticos.
 */

/**
 * EJERCICIO 3
 * Siguiendo el ejercicio anterior, en el main vamos a crear un ArrayList de Electrodomésticos
 * para guardar 4 electrodomésticos, ya sean lavadoras o televisores, con valores ya asignados.
 * 
 * Luego, recorrer este array y ejecutar el método precioFinal() en cada electrodoméstico. Se
 * deberá también mostrar el precio de cada tipo de objeto, es decir, el precio de todos los
 * televisores y el de las lavadoras. Una vez hecho eso, también deberemos mostrar, la suma del
 * precio de todos los Electrodomésticos. Por ejemplo, si tenemos una lavadora con un precio de
 * 2000 y un televisor de 5000, el resultado final será de 7000 (2000+5000) para
 * electrodomésticos, 2000 para lavadora y 5000 para televisor.
 */
package MAIN;

import Entidad.Electrodomestico;
import Entidad.Lavadora;
import Entidad.Televisor;
import java.util.ArrayList;
import java.util.Scanner;

public class HERENCIAEjercicioAprendizaje02 {

    public static void main(String[] args) {
       
        Scanner leer = new Scanner(System.in);
        
        ArrayList<Electrodomestico> Electrodomesticos = new ArrayList();
        
        int eleccion;
        String opcion;      
        
        /**
         * Siguiendo el ejercicio anterior, en el main vamos a crear un
         * ArrayList de Electrodomésticos para guardar 4 electrodomésticos, ya
         * sean lavadoras o televisores, con valores ya asignados.
         */
        
        do{

            System.out.println("¡Bienvenidx! ¿Que desea hacer?");
            System.out.println(" 1. Crear una lavadora");
            System.out.println(" 2. Crear un televisor");
            eleccion = leer.nextInt();
            
            switch (eleccion) {
                case 1:
                    Electrodomestico lava1 = new Lavadora();
                    lava1.crearElectrodomestico();
                    Electrodomesticos.add(lava1);
                    break;
                case 2:
                    Electrodomestico tv1 = new Televisor();
                    tv1.crearElectrodomestico();
                    Electrodomesticos.add(tv1);
                    break;
            }
            System.out.println("¿Desea ingresar algún otro electrodoméstico? S/N" );
            opcion = leer.next();
            
        }while(opcion.equalsIgnoreCase("S"));
        
        /**
         * Luego, recorrer este array y ejecutar el método precioFinal() en cada
         * electrodoméstico. Se deberá también mostrar el precio de cada tipo de
         * objeto, es decir, el precio de todos los televisores y el de las
         * lavadoras. Una vez hecho eso, también deberemos mostrar, la suma del
         * precio de todos los Electrodomésticos.
         */
        
        double precioTotal = 0;
        
        for (Electrodomestico aux : Electrodomesticos) {
            aux.precioFinal();
            System.out.println(aux.toString());
            precioTotal += aux.getPrecio();
        }

        System.out.println("El precio total de los electrodomésticos es $ " + precioTotal);
    }
    
}
