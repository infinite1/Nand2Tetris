import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class Parser {

//	private ArrayList<String> contents = new ArrayList<>();
	private Scanner fileInputStream;
	private String currentCommand;

	public Parser(String filePath) throws FileNotFoundException {
		fileInputStream = new Scanner(new FileInputStream(filePath));
	}

	public boolean hasMoreCommands() {
		return fileInputStream.hasNextLine();
	}

	public void advance() {
		currentCommand = fileInputStream.nextLine().replaceAll("\\s+", "");
	}

	public String getCurrentCommand() {
		return currentCommand;
	}

	// return the type of current command
	public String commandType() {
		if (currentCommand.startsWith("@")) {
			return "A_COMMAND";
		} else if (currentCommand.startsWith("(")){
			return "L_COMMAND";
		} else if (currentCommand.startsWith("//") || currentCommand.isEmpty()){
			return "Others";
		} else {
			return "C_COMMAND";
		}
	}

	public String symbol() {
		String instruct = currentCommand.split("//")[0];
		return instruct.substring(1);
	}

	public String dest() {
		String instruct = currentCommand.split("//")[0];
		if (instruct.contains("=")) {
			return instruct.split("=")[0];
		}
		return null;
	}

	public String comp() {
		String instruct = currentCommand.split("//")[0];
		if (!instruct.contains("=") && instruct.contains(";")) {
			return instruct.split(";")[0];
		} else {
			return instruct.split("[=;]")[1];
		}
	}

	public String jump() {
		String instruct = currentCommand.split("//")[0];
		if (instruct.contains(";") && !instruct.contains("=")) {
			return instruct.split(";")[1];
		} else if (instruct.contains(";") && instruct.contains("="))  {
			return instruct.split("[=;]")[2];
		}

		return null;
	}

	// check if symbol is numeric
	public boolean isNumeric(String symbol) {
		for (int i = 0; i < symbol.length(); i++) {
			if (!Character.isDigit(symbol.charAt(i))) {
				return false;
			}
		}
		return true;
	}
}
