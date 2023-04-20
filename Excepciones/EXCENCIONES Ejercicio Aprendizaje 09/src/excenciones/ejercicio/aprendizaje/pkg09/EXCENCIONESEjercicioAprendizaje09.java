/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package excenciones.ejercicio.aprendizaje.pkg09;

/**
 *
 * @author Usuario
 */
public class EXCENCIONESEjercicioAprendizaje09 {
//Dado el método metodoC de la clase C, indique:
//a) ¿Qué sentencias y en qué orden se ejecutan si se produce la excepción MioException?
    /**
     * De producirse MIOEXCEPTION el orden iria sentencia_c1, entra al try ejecuta sentencia_c2
     * y ejecuta sentencia_c3, catch de MIOEXCEPTION, sentencia_c4, y por último sentencia_c6
     */
//b) ¿Qué sentencias y en qué orden se ejecutan si no se produce la excepción MioException?
    /**
     * De NO producirse MIOEXCEPTION, el orden sería sentencia_c1, entra al try ejecuta sentencia_c2
     * y ejecuta sentencia_c3 y por último sentencia_c6
     */
//c) ¿Qué sentencias y en qué orden se ejecutan si se produce la excepción TuException?
    /**
     * Si se produce TUEXCEPTION, sentencia_c1, ejecuta el try con sentencia_C2 y sentencia_c3, ejecuta el
     * catch de TUEXCEPTION con la sentencia_c5 y finaliza con sentencia_c6
     */

    class C {

        void metodoC() throws Exception{ //TU
            //sentencia_c1
        try {
            //sentencia_c2
            //sentencia_c3
        } catch (Exception e){ //MIO
            //sentencia_c4
        } catch (Exception a){ //TU
            //sentencia_c5
            //throw (A)
        }
            //finally
            //sentencia_c6

}
}
}
