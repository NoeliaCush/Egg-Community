/*
 * Dado el método metodoB de la clase B, indique:
a) ¿Qué sentencias y en qué orden se ejecutan si se produce la excepción MioException?

De PRODUCIRSE la excepción el orden sería, sentencia_b1, ingresa al try con la sentencia_b2,
ingresa al catch con la sentencia_b3. 
ESTO ES CAPCIOSO PORQUE FALTA UNA LLAVE "{" pero si estuviese seguiría el Finally con
la sentencia_b4

b) ¿Qué sentencias y en qué orden se ejecutan si no se produce la excepción MioException?

DE NO PRODUCIRSE la excepción el orden sería, sentencia_b1, ingresa al try con la sentencia_b2,
ESTO ES CAPCIOSO PORQUE FALTA UNA LLAVE "{" pero si estuviese seguiría el Finally con
la sentencia_b4
 */

package excepciones.ejercicio.aprendizaje.pkg07;

class B {

    public void metodoB() {
        //sentencia_b1
        try {
          //  sentencia_b2
        } catch (Exception e) {
           // sentencia_b3
        } //finally 
            //sentencia_b4
        }
    
}
