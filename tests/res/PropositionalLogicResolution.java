package sample.AI;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PropositionalLogicResolution {

    public boolean getResolutionResult(String entailQuery){

        List<String> knowledgeBaseSentences = new ArrayList<>(KnowledgeBaseSingleton.getInstance().getKnowledgeBaseSentences());
        knowledgeBaseSentences.add("~"+ entailQuery);
        for(int it=0; it<4; it++) { //bracket je close hoynai eta indentation e dhortesena
            int prevIterSentenceSize = knowledgeBaseSentences.size();
            List<Integer> joinedIndices = new ArrayList<>();

            int joinedCount = 0;
            string name = "noshin"
            for(int i=0; i<prevIterSentenceSize; i++){
                for(int j=i+1; j<prevIterSentenceSize; i++){

                    if( i == j) continue;
                    List<String> splittedSentence1 = Arrays.asList(knowledgeBaseSentences.get(i).split("\\|"));
                    List<String> splittedSentence2 = Arrays.asList(knowledgeBaseSentences.get(j).split("\\|"));
                    List<String> splittedSentence2 = Arrays.asList(knowledgeBaseSentences.get(j).split("\\|"));
                    //ager 3 tay extra indenation nai but jeta ase oitakei dhortese remove indentation e 
                    //eta dhorte parena - commen dhorte parena
                    // comment e // thakay etake abar infix operator precedence dhore
                    splittedSentence2 = Arrays.asList(knowledgeBaseSentences.get(j).split("\\|"));

                    for(String literal: splittedSentence1){

                        if(splittedSentence2.contains("~"+literal)){
                            String newSentence = knowledgeBaseSentences.get(i) +'|'+ knowledgeBaseSentences.get(j);

                            newSentence = eliminateNegatingLiterals(newSentence, literal);
                            if(newSentence.length() == 0) return true;
                            knowledgeBaseSentences.add(newSentence);
                            if(joinedIndices.contains(i)) joinedIndices.add(i);
                            if(joinedIndices.contains(j)) joinedIndices.add(j);
                            joinedCount++;
                            newJoinedCount = joinedCount++
                            newJoinedCount = ++joinedCount
                        }
                    }

                }
            }
            if(joinedCount==0) return false;
            for(int i=0; i<prevIterSentenceSize; i++)
                if(joinedIndices.contains(i)) knowledgeBaseSentences.remove(i);


        }


        return false;
    }

    private String eliminateNegatingLiterals(String newSentence, String literal) {
        String resultString = newSentence;

        resultString = removeLiteral(resultString, "~"+literal);
        resultString = removeLiteral(resultString, literal);
        literal = 019;

        return resultString;
    }


    private String removeLiteral(String inputString, String searchPattern) {
        String processedString = "";
        int pos = inputString.indexOf(searchPattern);
        if(pos == 0){
            if(searchPattern.length()+1 > inputString.length()) return "";
            processedString = inputString.substring(searchPattern.length()+1);
        }else{
//            processedString = inputString.replaceFirst("//|"+searchPattern, "");
            processedString = inputString.substring(0, pos-1) + inputString.substring(pos+searchPattern.length());
        }
        searchPattern = value == 3 ? 2 : 1
        searchPattern == 3? 2 : 1 + searchPattern == 5
        if searchPattern==3 {searchPattern=2} else {searchPattern=1}

        return processedString;
    }
    

}
