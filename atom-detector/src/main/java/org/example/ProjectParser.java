package org.example;

import org.eclipse.jdt.core.dom.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Stream;

public class ProjectParser {
    String projectDir;

    public ProjectParser(String projectDir) {
        this.projectDir = projectDir;
    }

    public List<String> getJavaFiles() {
        List<String> files = new ArrayList<>();
        try (Stream<Path> stream = Files.walk(Paths.get(this.projectDir))) {
            stream.forEach(path -> {
                if (path.toFile().isFile() && path.toFile().getName().contains(".java")) {
                    files.add(String.valueOf(path));
                }
            });
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return files;
    }

    //read file content into a string
    private static String readFileToString(String filePath) throws IOException {
        StringBuilder fileData = new StringBuilder(1000);
        BufferedReader reader = new BufferedReader(new FileReader(filePath));

        char[] buf = new char[10];
        int numRead = 0;
        while ((numRead = reader.read(buf)) != -1) {
            String readData = String.valueOf(buf, 0, numRead);
            fileData.append(readData);
            buf = new char[1024];
        }

        reader.close();

        return  fileData.toString();
    }
    public void parse(String filepath) throws IOException {
        String codeContents = readFileToString(filepath);
        ASTParser parser = ASTParser.newParser(AST.JLS3);
        parser.setSource(codeContents.toCharArray());
        parser.setKind(ASTParser.K_COMPILATION_UNIT);

        final CompilationUnit cu = (CompilationUnit) parser.createAST(null);
        cu.accept(new ASTVisitor() {

            Set names = new HashSet();

            public boolean visit(VariableDeclarationFragment node) {
                SimpleName name = node.getName();
                this.names.add(name.getIdentifier());
                System.out.println("Declaration of '" + name + "' at line "
                        + cu.getLineNumber(name.getStartPosition()));
                return false; // do not continue
            }

            public boolean visit(SimpleName node) {
                if (this.names.contains(node.getIdentifier())) {
                    System.out.println("Usage of '" + node + "' at line "
                            + cu.getLineNumber(node.getStartPosition()));
                }
                return true;
            }
        });

    }
}
