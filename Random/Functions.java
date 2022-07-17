import java.util.Arrays;
import java.util.List;
import java.util.Collections;

public class Deck{
  List<String> deck;
  public Deck(){
    this.deck = Arrays.asList("s1","c1","d1","h1","s2","c2","d2","h2","s3","c3","d3","h3","s4","c4","d4","h4","s5","c5","d5","h5","s6","c6","d6","h6","s7","c7","d7","h7","s8","c8","d8","h8","s9","c9","d9","h9","s10","c10","d10","h10","s11","c11","d11","h11","s12","c12","d12","h12","s13","c13","d13","h13");
  }
  public void resetDeck(){
    Collections.shuffle(this.deck);
  }
}
