import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;


public class Rename {
  public static void main(String[] args) throws IOException {
	  Files.walk(Paths.get("/Users/danieldanciu/cb/laute")).forEach(filePath -> {
		    if (Files.isRegularFile(filePath)) {
		    	System.out.print("Rename " + filePath + " to: ");
		    	File original = filePath.toFile();
		    	File dest = new File(original.getAbsolutePath().replace("Ä", "Ae").replace("Ö", "Oe").replace("Ü", "Ue").replace("ü", "ue").replace("ö", "oe").replace("ä", "ae").replace(" ", "").toLowerCase());
				original.renameTo(dest);
		        System.out.println(dest);
		    }
		});
  }
}
