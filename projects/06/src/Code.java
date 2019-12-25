public class Code {

	public static String dest(String destStr) {
		String binCode = null;
		if (destStr == null) {
			binCode = "000";
		} else {
			switch (destStr) {
				case "M":
					binCode = "001";
					break;
				case "D":
					binCode = "010";
					break;
				case "MD":
					binCode = "011";
					break;
				case "A":
					binCode = "100";
					break;
				case "AM":
					binCode = "101";
					break;
				case "AD":
					binCode = "110";
					break;
				case "AMD":
					binCode = "111";
					break;
			}
		}
		return binCode;
	}


	public static String jump(String jumpStr) {
		String binCode = null;
		if (jumpStr == null) {
			binCode = "000";
		} else {
			switch (jumpStr) {
				case "JGT":
					binCode = "001";
					break;
				case "JEQ":
					binCode = "010";
					break;
				case "JGE":
					binCode = "011";
					break;
				case "JLT":
					binCode = "100";
					break;
				case "JNE":
					binCode = "101";
					break;
				case "JLE":
					binCode = "110";
					break;
				case "JMP":
					binCode = "111";
					break;
			}
		}
		return binCode;
	}

	public static String comp(String compStr) {
		String binCode = null;
		switch (compStr) {
			case "0":
				binCode = "0101010";
				break;
			case "1":
				binCode = "0111111";
				break;
			case "-1":
				binCode = "0111010";
				break;
			case "D":
				binCode = "0001100";
				break;
			case "A":
				binCode = "0110000";
				break;
			case "!D":
				binCode = "0001101";
				break;
			case "!A":
				binCode = "0110001";
				break;
			case "-D":
				binCode = "0001111";
				break;
			case "-A":
				binCode = "0110011";
				break;
			case "D+1":
				binCode = "0011111";
				break;
			case "A+1":
				binCode = "0110111";
				break;
			case "D-1":
				binCode = "0001110";
				break;
			case "A-1":
				binCode = "0110010";
				break;
			case "D+A":
				binCode = "0000010";
				break;
			case "D-A":
				binCode = "0010011";
				break;
			case "A-D":
				binCode = "0000111";
				break;
			case "D&A":
				binCode = "0000000";
				break;
			case "D|A":
				binCode = "0010101";
				break;
			case "M":
				binCode = "1110000";
				break;
			case "!M":
				binCode = "1110001";
				break;
			case "-M":
				binCode = "1110011";
				break;
			case "M+1":
				binCode = "1110111";
				break;
			case "M-1":
				binCode = "1110010";
				break;
			case "D+M":
				binCode = "1000010";
				break;
			case "D-M":
				binCode = "1010011";
				break;
			case "M-D":
				binCode = "1000111";
				break;
			case "D&M":
				binCode = "1000000";
				break;
			case "D|M":
				binCode = "1010101";
				break;
		}
		return binCode;
	}
}
