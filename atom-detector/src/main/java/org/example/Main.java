package org.example;

import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        ProjectParser pp = new ProjectParser("/media/fuad/CE62638F62637ADB/fuad/projects/atoms_of_confusion-SER/test_systems/ActionBarSherlock");
        try {
            pp.parse(pp.getJavaFiles().get(0));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}