package org.example.classifiers;

import org.eclipse.jdt.core.dom.ASTNode;

public class LiteralEncoding implements IAtomFinder{
    @Override
    public boolean detect(ASTNode node) {
        return false;
    }
}
