package org.example.classifiers;

import org.eclipse.jdt.core.dom.ASTNode;

public interface IAtomFinder {
    boolean detect(ASTNode node);
}
