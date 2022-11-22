package org.example.classifiers;

import org.eclipse.jdt.core.dom.ASTNode;

public class PreXcrement implements IAtomFinder{
    @Override
    public boolean detect(ASTNode node) {
        return false;
    }
}
