import java.util.*;

public class daisychains{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int numFlowers = in.nextInt();
        in.nextLine();

        Integer[] numPetals = new Integer[numFlowers];
        for(int i = 0; i < numFlowers; i++){
            numPetals[i] = in.nextInt();
        }

        System.out.println(avgFlower(numFlowers, numPetals));

        in.close();
    }

    public static int avgFlower(int flowers, Integer[] petals){
        int count = 0;
        for(int i = 0; i < flowers; i++){
            int tempSum = 0;
            for(int j = i; j < flowers; j++){
                tempSum += petals[j];
                int length = j - i + 1;
                if (tempSum % length == 0){
                    int average = tempSum / length;
                    for(int e = i; e < j+1; e++){
                        if (petals[e] == average){
                            count++;
                            break;
                        }
                    }
                }
            }
        }
        return count;
    }
}