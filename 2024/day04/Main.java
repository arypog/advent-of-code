import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.*;

public class Main {
    public static int[][] directions = {
        {0, 1},   // Right
        {0, -1},  // Left
        {1, 0},   // Down
        {-1, 0},  // Up
        {1, 1},   // Down-Right
        {1, -1},  // Down-Left
        {-1, 1},  // Up-Right
        {-1, -1}  // Up-Left
    };

    public static boolean checkWord(String[] map, int x, int y, int dx, int dy) {
        String xmas = "XMAS";
        int columns = map[0].length();
        int rows = map.length;

        for (int i = 0; i < xmas.length(); i++) {
            int nx = x + i * dx;
            int ny = y + i * dy;

            if (nx < 0 || nx >= rows || ny < 0 || ny >= columns || map[nx].charAt(ny) != xmas.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    public static int countWord(String[] map) {
        int columns = map[0].length();
        int rows = map.length;
        int total = 0;

        for (int x = 0; x < rows; x++) {
            for (int y = 0; y < columns; y++) {
                for (int[] dir : directions) {
                    if (checkWord(map, x, y, dir[0], dir[1])) {
                        ++total;
                    }
                }
            }
        }
        return total;
    }

    public static void main(String[] args) {
            try {
            //File f = new File("in/in.test");
            File f = new File("in/in.pub");
            Scanner sc = new Scanner(f);
            
            List<String> mapList = new ArrayList<>();
            while (sc.hasNextLine()) {
                String data = sc.nextLine();
                mapList.add(data);
            }

            String[] map = mapList.toArray(new String[0]);
            int total = countWord(map);
            System.out.println(total);

            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("ERROR WITH FILE.");
            e.printStackTrace();
        }
    }
}