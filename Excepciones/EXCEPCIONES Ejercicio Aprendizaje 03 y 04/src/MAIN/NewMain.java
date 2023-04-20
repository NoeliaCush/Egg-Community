package MAIN;


import ENTIDADES.DivisionNumero;
import java.util.InputMismatchException;
import java.util.Scanner;

public class NewMain {

    public static void main(String[] args) {
        
        try{
            Scanner leer = new Scanner(System.in); //ESCANER
        //Lectura numeros CADENA
        System.out.println("Por favor, ingrese los números en formato cadena");
        String numero1 = leer.nextLine();
        String numero2 = leer.nextLine();
        
        DivisionNumero division = new DivisionNumero();
        
        //Metodo PARSEINT()
        System.out.println("Pasando los números a INT");
        division.setNum1(Integer.parseInt(numero1));
        division.setNum2(Integer.parseInt(numero2));
      
        System.out.println("El resultado de la división es " + division.Division(division.getNum1(), division.getNum2()));
        } catch(InputMismatchException e){
            System.out.println("Error: " + e.getMessage());
        }catch(NumberFormatException e1){
            System.out.println("Error: " + e1.getMessage());
        }catch(ArithmeticException e2){
            System.out.println("Error: " + e2);
        }
    
        
        
    }
    
}
