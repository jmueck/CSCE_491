import java.util.Arrays;

public class VaultDoor8 {
    public static void main(String[] args) {
        VaultDoor8 a = new VaultDoor8();
        String unscrambledPassword = a.unscramblePassword(a.expected);
        String password = "aaaaaaaa" + unscrambledPassword + "a";
        if (a.checkPassword(password.substring(8, password.length() - 1))) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
        System.out.println("Password: " + password.substring(8, password.length() - 1));
    }

    char[] expected = {
        0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xE0, 0x95, 0xF1, 0xE1, 0xE0, 0xA4, 0xC0, 0x94, 0xA4
    };

    public char[] scramble(String password) {
        char[] a = password.toCharArray();
        for (int b = 0; b < a.length; b++) {
            char c = a[b];
            c = switchBits(c, 1, 2);
            c = switchBits(c, 0, 3);
            c = switchBits(c, 5, 6);
            c = switchBits(c, 4, 7);
            c = switchBits(c, 0, 1);
            c = switchBits(c, 3, 4);
            c = switchBits(c, 2, 5);
            c = switchBits(c, 6, 7);
            a[b] = c;
        }
        return a;
    }

    public char switchBits(char c, int p1, int p2) {
        char mask1 = (char)(1 << p1);
        char mask2 = (char)(1 << p2);
        char bit1 = (char)(c & mask1);
        char bit2 = (char)(c & mask2);
        char rest = (char)(c & ~(mask1 | mask2));
        char shift = (char)(p2 - p1);
        char result = (char)((bit1<<shift) | (bit2>>shift) | rest);
        return result;
    }

    public String unscramblePassword(char[] expected) {
        char[] unscrambled = new char[expected.length];
        for (int i = 0; i < expected.length; i++) {
            char c = expected[i];
            c = inverseSwitchBits(c, 6, 7);
            c = inverseSwitchBits(c, 2, 5);
            c = inverseSwitchBits(c, 3, 4);
            c = inverseSwitchBits(c, 0, 1);
            c = inverseSwitchBits(c, 4, 7);
            c = inverseSwitchBits(c, 5, 6);
            c = inverseSwitchBits(c, 0, 3);
            c = inverseSwitchBits(c, 1, 2);
            unscrambled[i] = c;
        }
        return new String(unscrambled);
    }

    public char inverseSwitchBits(char c, int p1, int p2) {
        char mask1 = (char)(1 << p1);
        char mask2 = (char)(1 << p2);
        char bit1 = (char)(c & mask2);
        char bit2 = (char)(c & mask1);
        char rest = (char)(c & ~(mask1 | mask2));
        char shift = (char)(p2 - p1);
        char result = (char)((bit1>>shift) | (bit2<<shift) | rest);
        return result;
    }

    public boolean checkPassword(String password) {
        char[] scrambled = scramble(password);
        return Arrays.equals(scrambled, expected);
    }
}