
public class GoodVsEvil {

  public static String battle(String goodAmounts, String evilAmounts) {

    String[] s_g = goodAmounts.split(" ");
    int[] m_g = new int[] { 1, 2, 3, 3, 4, 10 };

    int sum_good = 0;

    for (int i = 0; i < m_g.length; i++) {
      int v = Integer.parseInt(s_g[i]);
      if (v == 0) {
        continue;
      }

      sum_good += (v * m_g[i]);
    }

    String[] s_e = evilAmounts.split(" ");
    int[] m_e = new int[] { 1, 2, 2, 2, 3, 5, 10 };
    
    int sum_evil = 0;

    for (int i = 0; i < m_e.length; i++) {
      int v = Integer.parseInt(s_e[i]);
      if (v == 0) {
        continue;
      }

      sum_evil += (v * m_e[i]);
    }

    String result = "";

    if(sum_good == sum_evil){
      result = "Battle Result: No victor on this battle field";
    }
    else if (sum_good > sum_evil) {
      result = "Battle Result: Good triumphs over Evil";
    }else{
      result = "Battle Result: Evil eradicates all trace of Good";
    }

    return result;
  }
}