package Entidades;


import Entidades.Animal;

public class Perro extends Animal {

    public Perro(String string, String i, int i1, String string1) {
        super(string, i, i1, string1);
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

  
    public String getAlimento() {
        return alimento;
    }

    public void setAlimento(String alimento) {
        this.alimento = alimento;
    }

    
    
    @Override
    public void Alimentarse() {
        System.out.println( "Perro " + this.getNombre() + " se alimenta de " + this.getAlimento());
    }

    
}
