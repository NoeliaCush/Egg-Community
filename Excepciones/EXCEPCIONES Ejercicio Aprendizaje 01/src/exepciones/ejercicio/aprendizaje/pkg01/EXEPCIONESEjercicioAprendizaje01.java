/**
 * Inicializar un objeto de la clase Persona ejercicio 7 de la guía POO, a null y tratar de invocar el
 * método esMayorDeEdad() a través de ese objeto. Luego, englobe el código con una cláusula
 * try-catch para probar la nueva excepción que debe ser controlada.
 */
package exepciones.ejercicio.aprendizaje.pkg01;

import exepciones.ejercicio.aprendizaje.pkg01.Entidad.Persona;

public class EXEPCIONESEjercicioAprendizaje01 {

    public static void main(String[] args) {

        //Inicializamos el objeto a "NULL"
        Persona p1 = new Persona(null, 0, null, 0, 0);

        try {
            p1.esMayorDeEdad(); //Intento de INVOCACIÓN desde el objeto
        } catch (Exception e) { //Ha encontrado LA EXCEPCION
            System.out.println(e.getMessage()); //Mensaje PREDETERMINADO DE GET MESSAGE
        }

    }

}
