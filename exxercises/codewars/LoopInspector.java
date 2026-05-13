/* 
    @codewars ref: https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/java
*/

import java.util.HashSet;

public class LoopInspector {

    static class Node {
        Node val;

        public Node getNext() {
            return val;
        }
    }

    public int loopSize(Node node) {
        HashSet<Node> set = new HashSet<>();
        int c = 1;

        Node p = node;
        Node loopStart = null;

        while (p != null) {
            if (!set.add(p)) {
                loopStart = p;
                break;
            }
            p = p.getNext();
        }

        if (loopStart == null)
            return 0;

        p = loopStart.getNext();

        while (p != loopStart) {
            c++;
            p = p.getNext();
        }

        return c;
    }
}
