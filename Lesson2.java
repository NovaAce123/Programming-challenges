public class Lesson2 {
    public static void main(String[] args){
        yesloop();
        carloop();
        ifday();
        switchday();
        tryexcept();
    }

    public static void yesloop(){
        for (int i = 0; i < 5; i++){
            System.out.println("yes");
        }
    }

    public static void carloop(){
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for (String el : cars) {
            System.out.println(el);
        }
    }

    public static void ifday(){
        int day = 4;

        if (day == 6) {
            System.out.println("Today is Saturday");
        } else if (day == 7) {
            System.out.println("Today is Sunday");
        } else {
            System.out.println("looking forward to the weekend");
        }
    }

    public static void switchday(){
        int day = 4;
        switch(day) {
            case 6:
                System.out.println("Today is Saturday");
            case 7:
                System.out.println("Today is Sunday");
            default:
                System.out.println("looking forward to the weekend");
        }
    }

    public static void tryexcept(){
        int [] myNumbers = {1,2,3};
        try {
            System.out.println(myNumbers[10]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array Index is out of bounds " + e);
        }
    }
}
