/**
 * Se plantea desarrollar un programa que nos permita calcular el área y el perímetro de formas
 * geométricas, en este caso un círculo y un rectángulo. Ya que este cálculo se va a repetir en las
 * dos formas geométricas, vamos a crear una Interfaz, llamada calculosFormas que tendrá, los
 * dos métodos para calcular el área, el perímetro y el valor de PI como constante.
 */

package ENTIDAD;

public class calculosFormas {

    //ATRIBUTO CONSTANTE
    protected Double pi = (Math.PI);

    //CONSTRUCTORES
    public calculosFormas() {
    }

    //GETTER & SETTER
    public Double getPi() {
        return pi;
    }

    public void setPi(Double pi) {
        this.pi = pi;
    }

    //METODOS
    
    public void crearCirculo(){
        
    }
    
    public void crearRectangulo(){
        
    }
    
    public void calcularArea() {
    }

    public void calcularPerimetro() {
    }

}
