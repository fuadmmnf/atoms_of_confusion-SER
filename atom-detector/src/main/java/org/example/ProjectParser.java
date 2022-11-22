package org.example;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
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
}
