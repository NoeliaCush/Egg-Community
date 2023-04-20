/**
 * Desarrollar el ejercicio para que las formas implementen los métodos de la interfaz y se
 * calcule el área y el perímetro de los dos. En el main se crearán las formas y se mostrará el
 * resultado final.
 */
package MAIN;

import ENTIDAD.Circulo;
import ENTIDAD.Rectangulo;
import ENTIDAD.calculosFormas;
import java.util.Scanner;

public class NewMain {

    public static void main(String[] args) {
   
        Scanner leer = new Scanner(System.in);
        
        calculosFormas c1 = new Circulo();
        calculosFormas r1 = new Rectangulo();
        
        int respuesta;
       
        
        do{
            System.out.println("PROGRAMA DE CALCULO FORMAS GEOMÉTRICAS");
            System.out.println("Para crear un CIRCULO, presione 1");
            System.out.println("Para crear un RECTANGULO, presione 2");
            System.out.println("Para calcular el AREA de un CIRCULO, presione 3");
            System.out.println("Para calcular el AREA de un RECTANGULO, presione 4");
            System.out.println("Para calcular el PERIMETRO de un CIRCULO, presione 5");
            System.out.println("Para calcular el PERIMETRO de un RECTANGULO, presione 6");
            System.out.println("Para SALIR, presione 7");
            System.out.println(" ");
            
            respuesta = leer.nextInt();

            switch (respuesta) {
                case 1:
                    System.out.println("Por favor, para crear un CIRCULO complete los siguientes datos");
                    c1.crearCirculo();
                    break;
                case 2:
                    System.out.println("Por favor, para crear un RECTANGULO complete los siguientes datos");
                    r1.crearRectangulo();
                    break;
                case 3:
                    System.out.println("La FÓRMULA para calcular el AREA de un Círculo es: PI*radio²");
                    c1.calcularArea();
                    break;
                case 4:
                    System.out.println("La FÓRMULA para calcular el AREA de un Rectángulo es: base * altura");
                    r1.calcularArea();
                    break;
                case 5:
                    System.out.println("La FÓRMULA para calcular el PERIMETRO de un Círculo es: PI * diámetro");
                    c1.calcularPerimetro();
                    break;
                case 6:
                    System.out.println("La FÓRMULA para calcular el PERIMETRO de un Rectángulo es: (base + altura) * 2");
                    r1.calcularPerimetro();
                    break;
            }

        } while (respuesta != 7);

    }

}
