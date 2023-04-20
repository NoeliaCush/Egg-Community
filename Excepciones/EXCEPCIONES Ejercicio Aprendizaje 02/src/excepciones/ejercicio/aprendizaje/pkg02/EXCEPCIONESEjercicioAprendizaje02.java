/**
 * Definir una Clase que contenga algún tipo de dato de tipo array y agregue el código para
 * generar y capturar una excepción ArrayIndexOutOfBoundsException (índice de arreglo fuera
 * de rango).
 */
package excepciones.ejercicio.aprendizaje.pkg02;

public class EXCEPCIONESEjercicioAprendizaje02 {

    public static void main(String[] args) {

        int grados[] = {1, 2, 3, 4, 5, 6};

        try {
            System.out.println("El 6to año se encuentra en la pocisión " + grados[6]);
        } catch (ArrayIndexOutOfBoundsException a) {
            System.out.println("INDICE DE ARREGLO FUERA DE RANGO!!");
            System.out.println("Error: " + a);
        }
    }

}
