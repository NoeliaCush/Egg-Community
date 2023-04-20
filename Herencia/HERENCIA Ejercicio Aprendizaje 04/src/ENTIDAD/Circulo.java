package ENTIDAD;
import java.util.Scanner;

public final class Circulo extends calculosFormas {
    
    Scanner leer = new Scanner(System.in);
    
    //Área circulo: PI * radio ^ 2 / Perímetro circulo: PI * diámetro.
    
    //ATRIBUTOS
    private Double radio;
    private Double diametro;
    
    //GETTER & SETTER

    public Double getRadio() {
        return radio;
    }

    public void setRadio(Double radio) {
        this.radio = radio;
    }

    public Double getDiametro() {
        return diametro;
    }

    public void setDiametro(Double diametro) {
        this.diametro = diametro;
    }

    //METODOS
    @Override
    public void crearCirculo() {
        System.out.println("Valor RADIO: ");
        this.setRadio(leer.nextDouble());
        System.out.println("Valor DIAMETRO");
        this.setDiametro(leer.nextDouble());
    }
       
    @Override
    public void calcularPerimetro() {
        System.out.println("El valor del PERIMETRO del CIRCULO es = " + (this.getPi() * this.getDiametro()));
    }

    @Override
    public void calcularArea() {
        System.out.println("El valor del AREA del CIRCULO es = " + (this.getPi() * Math.pow(this.getRadio(), 2)));
    }

    

 
    
    
}
