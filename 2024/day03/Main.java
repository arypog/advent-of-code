import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static int mult_part1(String data) {
        int sum = 0;
        Pattern p = Pattern.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)", 
                                    Pattern.CASE_INSENSITIVE);
        Matcher m = p.matcher(data);

        while (m.find()) {
            int a = Integer.parseInt(m.group(1));
            int b = Integer.parseInt(m.group(2));
            sum += a*b;
        }
        return sum;
    }

    public static boolean flag = true;
    public static int mult_part2(String data) {
        int sum = 0;
        Pattern p_mul_do_dont = Pattern.compile("do\\(\\)|don't\\(\\)|mul\\((\\d{1,3}),(\\d{1,3})\\)", 
                                                Pattern.CASE_INSENSITIVE);
        Matcher m = p_mul_do_dont.matcher(data);

        while (m.find()) {
            if (m.group().equals("do()")) {
                flag = true;
            }
            
            if (m.group().equals("don't()")) {
                flag = false;
            }

            if (flag == true && !m.group().equals("do()")){
                int a = Integer.parseInt(m.group(1));
                int b = Integer.parseInt(m.group(2));
                sum += a*b;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        try {
            //File f = new File("in/in.test");
            File f = new File("in/in.pub");
            Scanner sc = new Scanner(f);
            
            int sum = 0;
            while (sc.hasNextLine()) {
                String data = sc.nextLine();
                sum += mult_part2(data);
            }
            System.out.println(sum);
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("ERROR WITH FILE.");
            e.printStackTrace();
        }
    }
}