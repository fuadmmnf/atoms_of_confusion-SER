package org.example;

import org.example.classifiers.IAtomFinder;

public class Atom {
    String name;
    IAtomFinder finder;

    public Atom(String name, IAtomFinder finder) {
        this.name = name;
        this.finder = finder;
    }
}
