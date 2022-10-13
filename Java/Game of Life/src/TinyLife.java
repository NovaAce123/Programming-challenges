public class TinyLife {
    public static void main(String[] args) throws Exception {

    }
    public static boolean getCell(long world, int col, int row) {

    }
    public static long setCell(long world, int col, int row, boolean value) {

    }
    public static void print(long world) {
        System.out.println("_");
        for (int row = 0; row < 8; row++){
            for (int col = 0; col < 8; col++) {
                System.out.print(getCell(world,col, row) ? "#" : "_");
            }
        }
        System.out.println();
    }
    public static int countNeighbours(long world, int col, int row) {

    }
    public static boolean computeCell(long world, int col, int row) {

    }
    public static long nextGeneration(long world){

    }
}
