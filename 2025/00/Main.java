import java.io.File;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        File f = new File("2025/00/pub");
        Scanner sc = new Scanner(f);
        System.out.println(sc.nextLine());
        sc.close();
    } 
}
