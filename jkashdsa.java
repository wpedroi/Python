package varib;

import javax.swing.JOptionPane;

static char ch;

public class Varib{

    public static void main(String[] args){

        string word = JOptionPane.showInputDialog( "Enter the name ");
        

        for (int i = 0; i < word.length(); i++){
            ch = word.charat(i);
            
            if (!Character.Isletter(ch)){
                word = JOptionPane.showInputDialog( "Enter the name again");
                i = -1;
            }

        }
        string age = JOptionPane.showInputDialog( "Enter the age ");

        for (int i = 0; i < age.length(); i++){
            ch = age.charat(i);
            
            if (!Character.IsDigit(ch)){
                age = JOptionPane.showInputDialog( "Enter the age again");
                i = -1;
            }

        }

    JOptionPane.showMessegeDialog(null, word + age);

    }

}