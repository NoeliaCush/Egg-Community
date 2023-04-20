/*
 Crear una superclase llamada Electrodoméstico con los siguientes atributos: precio, color, 
consumo energético (letras entre A y F) y peso.
 */
package Entidad;

import java.util.Scanner;

public class Electrodomestico {

    Scanner leer = new Scanner(System.in);   
    
    //Atributos
    protected double precio;
    protected String color;
    protected Character consumoEnergetico;
    protected double peso;

    /**
     * Los constructores que se deben implementar son los siguientes: • Un
     * constructor vacío. • Un constructor con todos los atributos pasados por
     * parámetro.
     */
    public Electrodomestico() {
    }

    public Electrodomestico(double precio, String color, Character consumoEnergetico, double peso) {
        this.precio = precio;
        this.color = color;
        this.consumoEnergetico = consumoEnergetico;
        this.peso = peso;
    }

    //METODOS
    //• Métodos getters y setters de todos los atributos.
    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public Character getConsumoEnergetico() {
        return consumoEnergetico;
    }

    public void setConsumoEnergetico(Character consumoEnergetico) {
        this.consumoEnergetico = consumoEnergetico;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    /**
     * Método comprobarConsumoEnergetico(char letra): comprueba que la letra es
     * correcta, sino es correcta usara la letra F por defecto.Este método se
     * debe invocar al crear el objeto y no será visible.
     *
     * @param letra
     */
    public void comprobarConsumoEnergetico(char letra) {

        if (letra == 'A' || letra == 'a' || letra == 'B' || letra == 'b' || letra == 'C' || letra == 'c' || letra == 'D' || letra == 'd' || letra == 'E' || letra == 'e' || letra == 'F' || letra == 'f') {
            this.consumoEnergetico = letra;
        } else {
            this.consumoEnergetico = 'F';
            System.out.println("El consumo energético del electrodoméstico por defecto es " + this.consumoEnergetico);
        }
    }
    
    /**
     * Método comprobarColor(String color): comprueba que el color es correcto,
     * y si no lo es, usa el color blanco por defecto.Los colores disponibles
     * para los electrodomésticos son blanco, negro, rojo, azul y gris. No
     * importa si el nombre está en mayúsculas o en minúsculas. Este método se
     * invocará al crear el objeto y no será visible.
     *
     * @param color
     */
    public void comprobarColor (String color){
        
        if(color.equalsIgnoreCase("BLANCO")|| color.equalsIgnoreCase("NEGRO") || color.equalsIgnoreCase("ROJO") || color.equalsIgnoreCase("AZUL") || color.equalsIgnoreCase("GRIS")){
            this.color = color;
        }else{
            this.color = "BLANCO";
            System.out.println("El color por defecto es " + this.color);
        }
    }

    /**
     * Metodo crearElectrodomestico(): le pide la información al usuario y llena
     * el electrodoméstico, también llama los métodos para comprobar el color y
     * el consumo. Al precio se le da un valor base de $1000.
     */
    
    public void crearElectrodomestico(){
  
        System.out.println("Por favor, indique el color del electrodoméstico");
        this.setColor(leer.next());
        comprobarColor(color);
        System.out.println("Por favor, indique el consumo energético del electrodomisto siendo A, B, C, D, E o F");
        this.setConsumoEnergetico(leer.next().charAt(0));
        comprobarConsumoEnergetico(consumoEnergetico);
        System.out.println("Por favor, inque el peso del electrodoméstico");
        this.setPeso(leer.nextDouble());
        System.out.println("El peso del electrodoméstico es " + this.getPeso() + " kg");
        this.precio =1000d;   
    }
    
    /**
     * Método precioFinal(): según el consumo energético y su tamaño, aumentará
     * el valor del precio. Esta es la lista de precios:
     */
    
    public void precioFinal(){
       
        //Según consumo energético
        
        switch(this.getConsumoEnergetico()){
            case 'A':
            case 'a':
                this.precio = this.precio + 1000;
                break;
            case 'B':
            case 'b':
                this.precio = this.precio + 800;
                break;
            case 'C':
            case 'c':
                this.precio = this.precio + 600;
                break;
            case 'D':
            case 'd':
                this.precio = this.precio + 500;
                break;
            case 'E':
            case 'e':
                this.precio = this.precio + 300;
                break;
            case 'F':
            case 'f':
                this.precio = this.precio + 100;
                break;               
        }
        
        //Según peso del electrodoméstico
     
        if(this.getPeso()>= 1 && this.getPeso()<=19){
             this.precio = this.precio + 100;
        }else if(this.getPeso()>= 20 && this.getPeso() <=49){
            this.precio = this.precio + 500;
        }else if(this.getPeso() >=50 && this.getPeso() <= 79){
            this.precio = this.precio + 800;
        }else if(this.getPeso() >=80){
            this.precio = this.precio + 1000;
        }
        
        //System.out.println("El precio Final del electrodoméstico es $ " + this.precio);
        
        
    }    

    @Override
    public String toString() {
        return "Electrodomestico{" + "leer=" + leer + ", precio=" + precio + ", color=" + color + ", consumoEnergetico=" + consumoEnergetico + ", peso=" + peso + '}';
    }
    
}
