import java.util.*;

public class udderedbutnotherd{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String cowphabet = in.nextLine();
        String word = in.nextLine();
        
        in.close();

        System.out.println(cycles(cowphabet, word));

    }

    public static int cycles(String ab, String w){
        int count = 0;
        int i = 0;
        while(i < w.length()){
            for(int j = 0; j < ab.length(); j++){
                if (w.charAt(i) == ab.charAt(j)){
                    i++;
                    if(i == w.length()) 
                        break;
                }
            }
            count++;
        }
        return count;
        }
}