/*
    Escribe una función que reciba dos palabras (String) y retorne
    verdadero o falso (Bool) según sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
*/

#include <iostream>
#include <string>
#include <vector>

std::string sortString(std::string s) {
  int i = 0;

  while (i < s.size()) {
    if (i == 0 || s[i] >= s[i - 1]) {
      i++;
    } else {
      char temp = s[i];
      s[i] = s[i - 1];
      s[i - 1] = temp;
      i--;
    }
  }
  return s;
}

bool anagram(const std::string &word1, const std::string &word2) {
  if (word1 == word2) {
    return false;
  }

  std::vector<char> c1(word1.size());
  std::string s1 = word1;
  std::string s2 = word2;

  return sortString(s1) == sortString(s2);
}

int main() {

  std::string v1 = "cara";
  std::string v2 = "arca";

  std::cout << "Result: " << std::boolalpha << anagram(v1, v2) << '\n';

  return 0;
}
