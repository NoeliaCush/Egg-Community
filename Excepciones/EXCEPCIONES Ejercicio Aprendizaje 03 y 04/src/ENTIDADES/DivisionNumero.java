/**
 * Defina una clase llamada DivisionNumero. En el método main utilice un Scanner para leer dos
 * números en forma de cadena. A continuación, utilice el método parseInt() de la clase Integer,
 * para convertir las cadenas al tipo int y guardarlas en dos variables de tipo int. Por ultimo realizar
 * una división con los dos numeros y mostrar el resultado.
 */
package ENTIDADES;

public class DivisionNumero { //CLASE DEFINIDA

    //ATRIBUTOS NUMEROS
    private int num1;
    private int num2;

    //CONSTRUCTORES
    public DivisionNumero() {
    }

    public DivisionNumero(int num1, int num2) {
        this.num1 = num1;
        this.num2 = num2;
    }
    
    //GETTER & SETTER

    public int getNum1() {
        return num1;
    }

    public void setNum1(int num1) {
        this.num1 = num1;
    }

    public int getNum2() {
        return num2;
    }

    public void setNum2(int num2) {
        this.num2 = num2;
    }
    
    //METODO DIVISION
    public double Division(int numero1, int numero2){
        
        double rdoDivision = numero1/numero2;
       
        return rdoDivision;
        
    }
    
    
    
   
}
