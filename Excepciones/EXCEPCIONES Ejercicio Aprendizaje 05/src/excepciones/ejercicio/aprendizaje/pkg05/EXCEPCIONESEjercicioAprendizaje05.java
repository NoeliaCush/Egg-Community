/**
 * Escribir un programa en Java que juegue con el usuario a adivinar un número. La computadora
 * debe generar un número aleatorio entre 1 y 500, y el usuario tiene que intentar adivinarlo. Para
 * ello, cada vez que el usuario introduce un valor, la computadora debe decirle al usuario si el
 * número que tiene que adivinar es mayor o menor que el que ha introducido el usuario. Cuando
 * consiga adivinarlo, debe indicárselo e imprimir en pantalla el número de veces que el usuario
 * ha intentado adivinar el número. Si el usuario introduce algo que no es un número, se debe
 * controlar esa excepción e indicarlo por pantalla. En este último caso también se debe contar el
 * carácter fallido como un intento.
 */
package excepciones.ejercicio.aprendizaje.pkg05;

import java.util.InputMismatchException;
import java.util.Scanner;

public class EXCEPCIONESEjercicioAprendizaje05 {

    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);

        int adivinar = (int) (Math.random() * 500) + 1; //genera num aleatoria entre 1 a 50

        System.out.println("num " + adivinar);

        int respuesta = 0; // introducir un valor;

        int intentos = 0; //por cada intento hay que sumar intentos++

        do {
            
            System.out.println("Ingrese un valor entre 1 y 500");

            try {
                respuesta = leer.nextInt();

                if (adivinar > respuesta) {
                    System.out.println("El número incógnico es MAYOR al ingresado!");

                } else if (adivinar < respuesta) {
                    System.out.println("El número incógnico es MENOR al ingresado!");
                }
            } catch (InputMismatchException e) {
                System.out.println("Error: Debe ingresar un número entero");
            } finally {
            }
            
            System.out.println("No lo adivinaste aún, volvé a intentar!");
            intentos++;
        } while (respuesta != adivinar);

        System.out.println("Felicidades, adivinaste el número " + adivinar);
        System.out.println("Tuviste un total de " + intentos + " intentos!");

    }

}
