import java.io.FileWriter;

public class Main{
    public static void main(String args[]){
       String str = "'Danka', 13, 13";
         try{
           FileWriter fw=new FileWriter("file1.csv");
           fw.write(str);
           fw.close();
          }catch(Exception e){System.out.println(e);}
          System.out.println("Success...");
     }
}
