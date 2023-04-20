package ENTIDAD;

import java.util.Scanner;

public final class Rectangulo extends calculosFormas {

    Scanner leer = new Scanner(System.in);
    
    //Área rectángulo: base * altura / Perímetro rectángulo: (base + altura) * 2.
    
    //ATRIBUTOS
    private Double base;
    private Double altura;
    
    //GETTER & SETTER

    public Double getBase() {
        return base;
    }

    public void setBase(Double base) {
        this.base = base;
    }

    public Double getAltura() {
        return altura;
    }

    public void setAltura(Double altura) {
        this.altura = altura;
    }
    
    //METODOS
    @Override
    public void crearRectangulo() {
        
        System.out.println("Valor BASE");
        this.setBase(leer.nextDouble());
        System.out.println("Valor ALTURA");
        this.setAltura(leer.nextDouble());
    }

    @Override
    public void calcularPerimetro() {  
        System.out.println("El valor del PERIMETRO del RECTANGULO es = " + ((this.getBase() + this.getAltura())* 2));
    }

    @Override
    public void calcularArea() {
        System.out.println("El valor del AREA del RECTANGULO es = " + (this.getAltura() * this.getBase()));
    }
    
    
    
    
    
}
