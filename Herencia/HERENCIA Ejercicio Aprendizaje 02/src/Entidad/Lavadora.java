/**
 * A continuación, se debe crear una subclase llamada Lavadora, con el atributo carga,
 * además de los atributos heredados.
 */
package Entidad;

import java.util.Scanner;

public final class Lavadora extends Electrodomestico{
    
    Scanner leer = new Scanner(System.in);
    
    private double carga; //Cantidad de kilos que soporta el lavaropas

    /**
     * Los constructores que se implementarán serán: 
     * • Un constructor vacío
     * • Un constructor con la carga y el resto de los atributos heredados.Recuerda que debes llamar al constructor de la clase padre.
     */

    public Lavadora() {
    }

    public Lavadora(double carga, double precio, String color, Character consumoEnergetico, double peso) {
        super(precio, color, consumoEnergetico, peso);
        this.carga = carga;
    }
    
    //METODOS
    
    //• Método get y set del atributo carga.

    public double getCarga() {
        return carga;
    }

    public void setCarga(double carga) {
        this.carga = carga;
    }
    
    /**
     * • Método crearLavadora (): este método llama a crearElectrodomestico() de
     * la clase padre, lo utilizamos para llenar los atributos heredados del
     * padre y después llenamos el atributo propio de la lavadora.
     */
   
    
    
    @Override
    public void crearElectrodomestico(){
        super.crearElectrodomestico();
        System.out.println("Por favor, ingrese el tamaño de la carga del lavaropas");
        this.setCarga(leer.nextDouble());
        System.out.println("El lavaropas tiene una carga de " + this.getCarga() + " kg");
    }
    
    /**
     * • Método precioFinal(): este método será heredado y se le sumará la
     * siguiente funcionalidad. Si tiene una carga mayor de 30 kg, aumentará el
     * precio en $500, si la carga es menor o igual, no se incrementará el
     * precio. Este método debe llamar al método padre y añadir el código
     * necesario. Recuerda que las condiciones que hemos visto en la clase
     * Electrodoméstico también deben afectar al precio.
     */
    
    @Override
    public void precioFinal() {
        super.precioFinal(); 
        
        if(this.carga>30){
            this.precio = this.precio + 500;
        } else {
           
        }
            
        
        System.out.println("El precio FINAL del lavaropas es $ " + this.precio );
           
    }

    @Override
    public String toString() {
        return super.toString(); //To change body of generated methods, choose Tools | Templates.
    }

  
    
    
}
