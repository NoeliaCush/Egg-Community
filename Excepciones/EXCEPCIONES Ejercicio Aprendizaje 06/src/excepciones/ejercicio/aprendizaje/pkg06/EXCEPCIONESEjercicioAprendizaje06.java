package excepciones.ejercicio.aprendizaje.pkg06;

public class EXCEPCIONESEjercicioAprendizaje06 {

    //Dado el método metodoA de la clase A, indique:
    //a) ¿Qué sentencias y en qué orden se ejecutan si se produce la excepción MioException?
    /**
     * En caso de que SE PRODUZCA la excepción, el orden sería: sentencia_1, setencia_2, ingresa al try y
     * continúa con las sentencias 3 y 4 que indicarán que hay una excepción (MIOEXCEPTION) la cual la setencia_6 dentro del catch 
     * mostaría el tipo de error y, por último, la sentencia 5.
     */
    //b) ¿Qué sentencias y en qué orden se ejecutan si no se produce la excepción MioException?
    /**
     * En el caso en que NO SE PRODUZCA LA EXCEPCION, el orden sería el siguiente, sentencia_1, sentencia2, entra al try
     * con la sentencia_3 y sentencia_4 y termina con sentencia_5
     */
    class A {

        public void metodoA() {

            //sentencia_a1 
            //sentencia_a2
            try {
                //sentencia_a3
                //sentencia_a4
            } catch (Exception e) {
                //sentencia_a6
            }
            //sentencia_a5
        }
    }

}
