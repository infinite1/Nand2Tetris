import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        try {
            SymbolTable symbolTable = new SymbolTable();

            // first pass, read label commands
            Parser firstParser = new Parser(args[0]);
            int romAddr = -1;
            while (firstParser.hasMoreCommands()) {
                firstParser.advance();
                if (firstParser.commandType().equals("A_COMMAND") ||
                firstParser.commandType().equals("C_COMMAND")) {
                    romAddr += 1;
                } else if (firstParser.commandType().equals("L_COMMAND")) {
                    String currentCMD = firstParser.getCurrentCommand();
                    String symbol = currentCMD.substring(1, currentCMD.length()-1);
                    int address = romAddr + 1;
                    symbolTable.addEntry(symbol, address);
                }
            }

            // second pass, read variable and translate
            Parser secondParser = new Parser(args[0]);
            int symbolAddress = 16; // allocate variable address
            ArrayList<String> output = new ArrayList<>();   // store binary code
            while (secondParser.hasMoreCommands()) {
                secondParser.advance();
                if (secondParser.commandType().equals("A_COMMAND")) {
                    String symbol = secondParser.symbol();
                    if (!secondParser.isNumeric(symbol)) {
                        if (symbolTable.contains(symbol)) {
                            String binCode = Integer.toBinaryString(symbolTable.getAddress(symbol));
                            String code = ("0000000000000000" + binCode).substring(binCode.length());
                            output.add(code);
                        } else {
                            symbolTable.addEntry(symbol, symbolAddress);
                            symbolAddress++;
                            String binCode = Integer.toBinaryString(symbolTable.getAddress(symbol));
                            String code = ("0000000000000000" + binCode).substring(binCode.length());
                            output.add(code);
                        }
                    } else {
                        String binCode = Integer.toBinaryString(
                                Integer.parseInt(symbol));
                        String code = ("0000000000000000" + binCode).substring(binCode.length());
                        output.add(code);
                    }
                } else if (secondParser.commandType().equals("C_COMMAND")) {
                    String code = "111" + Code.comp(secondParser.comp()) +
                            Code.dest(secondParser.dest()) + Code.jump(secondParser.jump());
                    output.add(code);
                }
            }

            String outFileName = args[0].replace("asm", "hack");
            String outputStr = String.join("\n", output);
            BufferedWriter writer = new BufferedWriter(new FileWriter(outFileName));
            writer.write(outputStr);
            writer.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
