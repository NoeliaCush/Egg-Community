/**
 * Se debe crear también una subclase llamada Televisor con los siguientes atributos:
 * resolución (en pulgadas) y sintonizador TDT (booleano), además de los atributos
 * heredados.
 */
package Entidad;

import java.util.Scanner;

public final class Televisor extends Electrodomestico{
    
    private double resolucion;
    private boolean sintonizadorTDT;

    /**
     * Los constructores que se implementarán serán:
     * • Un constructor vacío. 
     * • Un constructor con la resolución, sintonizador TDT y el resto de los
     * atributos heredados. Recuerda que debes llamar al constructor de la clase
     * padre.
     */

    public Televisor() {
    }

    Scanner leer = new Scanner(System.in);
        
    public Televisor(double resolucion, boolean sintonizadorTDT, double precio, String color, Character consumoEnergetico, double peso) {
        super(precio, color, consumoEnergetico, peso);
        this.resolucion = resolucion;
        this.sintonizadorTDT = sintonizadorTDT;
    }
    
    //METODOS
    
    //• Método get y set de los atributos resolución y sintonizador TDT.

    public double getResolucion() {
        return resolucion;
    }

    public void setResolucion(double resolucion) {
        this.resolucion = resolucion;
    }

    public boolean isSintonizadorTDT() {
        return sintonizadorTDT;
    }

    public void setSintonizadorTDT(boolean sintonizadorTDT) {
        this.sintonizadorTDT = sintonizadorTDT;
    }

     /**
     * • Método crearTelevisor(): este método llama a crearElectrodomestico() de
     * la clase padre, lo utilizamos para llenar los atributos heredados del
     * padre y después llenamos los atributos del televisor.
     */

    @Override
    public void crearElectrodomestico() {
        
        super.crearElectrodomestico(); 
        System.out.println("Por favor, ingrese la RESOLUCIÓN (cantidad de púlgadas) que tiene el televisor");
        this.setResolucion(leer.nextDouble());
        System.out.println("Es televisor tiene " + this.getResolucion() + " pulgadas");
        System.out.println("Por favor, indique si el codificador un sintonizador de cable TDT (S/N)");
        String opcion = leer.next();
        if(opcion.equalsIgnoreCase("S")){
            this.sintonizadorTDT = true;
            System.out.println("El televisor tiene sintonizador de cable TDT");
        }else{
            this.sintonizadorTDT = false;
            System.out.println("El televisor no tiene sintonizador de cable TDT");
        }   
    }

    /**
     * • Método precioFinal(): este método será heredado y se le sumará la
     * siguiente funcionalidad. Si el televisor tiene una resolución mayor de 40
     * pulgadas, se incrementará el precio un 30% y si tiene un sintonizador TDT
     * incorporado, aumentará $500. Recuerda que las condiciones que hemos visto
     * en la clase Electrodomestico también deben afectar al precio.
     */
    
    @Override
    public void precioFinal() {
        super.precioFinal(); 
        
        if(this.resolucion>40){
            this.precio = this.precio + (this.precio * 0.30);
        }else{
            
        }
        
        if(this.sintonizadorTDT){
            this.precio = this.precio + 500;
        }else{
            
        }
      
        System.out.println("El precio FINAL del televisor es $ " + this.precio);
        
    }
    
    

    
}
