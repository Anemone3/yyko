import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class _03_structure_data {
    public static void main(String[] args) {
        // lists();
        // maps();
        sets();
    }

    static void lists() {
        /* all list */
        List<Integer> arrList = new ArrayList<Integer>(Arrays.asList(1, 2, 3));
        var size = arrList.size(); // nos retorna el tamaño del array
        System.out.println("método size nos retorna el tamaño del array: " + size);
        var get = arrList.get(1); // nos retorna el valor segun el indice
        System.out.println("get(index) nos retorna el valor segun el indice: " + get);
        var remove = arrList.remove(2);// remueve el valor segun el indice
        System.out
                .println("el remove(index) nos quita el elemento del array y nos devuelve ese mismo numero: "
                        + remove);
        /// arrayList.iterator(); // TODO: aprender sobre iterator
        var arrEquals = arrList.equals(List.of(1, 2));
        System.out.println("equals(Object) nos compara una clase que tenga los mismos elementos: " + arrEquals);
        var contain = arrList.contains(2);
        System.out.println("contain(Object) si contiene un elemento retorna true: " + contain);
        var contains = arrList.containsAll(List.of(1));
        System.out.println(
                "containsAll(Collection) nos retorna true si la collection contiene lo mismo que la lista: "
                        + contains);
        System.out.println(
                "Diferencia de equals(Object) y containsAll(Collection) en equals importa los mismos elementos,orden y tamaño. A diferencia de containsAll no le importa el tamaño ni el orden, solo los elementos");
        arrList.reversed();
        System.out.println("reversed() nos retorna una lista revertida");
        arrList.set(1, 2);
        System.out.println("set(index,element) nos permite cambiar el valor en el indice indicado");

    }

    static void maps() {
        /* ============= Interfaz Map ============= */

        /* ============= HashMap ============= */
        Map<String, String> players = new HashMap<>();
        players.put("ariku", "lvl 1"); // agregar un elemento al hashmap
        var findByKey = players.get("ariku");
        System.out.println("metodo get(key) para obtener el value de ese key del hashmap: " + findByKey);
        players.put("ariku", "lvl 2");
        players.put("shiina", "lvl 1");
        System.out.println(
                "igualmente podemos usar el put para agregar o reemplazar segun su key, tambien nos retorna el valor agregado "
                        + players);
        var size = players.size();
        System.out.println("size() nos retorna la cantidad de elementos de nuestro HashMap " + size);
        var containsKey = players.containsKey("ariku");
        System.out.println(
                "containsKey(string) nos retorna true si existe una key con el parametro enviado"
                        + containsKey);
        var containsValue = players.containsValue("lvl 2");
        System.out.println(
                "containsValue(string) nos retorna un boolean si existe un valor con el parametro enviado"
                        + containsValue);
        var setValues = players.entrySet();
        System.out
                .println("entrySet() nos retorna un Set iterable [key=value], " + setValues);
        var keyValues = players.keySet();
        System.out.println("keySet() nos retorna un Set iterable de solo [keys] " + keyValues);
        var valueOrDefault = players.getOrDefault("arik", "ESTE_ES_UN_STRING_DEFAULT");
        System.out.println(
                "getOrDetaul(key,defaultString) te busca el valor si no se encuentra te retorna el default que asignaste, "
                        + valueOrDefault);

        /* Usando computeIf */
        Map<String, List<String>> mapB = new HashMap<>();
        mapB.computeIfAbsent("letras", key -> new ArrayList<>()).add("A");

        /*
         * Lo que hace aqui es buscar segun su key computeIfAbsten(KEY, callback), sino
         * existe la key en el map
         * lo que hará a continuacion es agregar al map esa key con su value key-> , en
         * este caso inicializamos
         * una lista, y despues de este metodo usamos add, osea que si ya se encontró la
         * key, nos retorna su VALUE
         * y pues uso .add() porque el Value es una List, y agrego elemento, es como un
         * if(mapB.containsKey()){
         * var value = mapB.get("letras");
         * value.add("A")
         * }else{
         * mapB.put("letras",new ArrayList());
         * }
         * esto seria la version larga, y la version corta con computeIfAbsent
         * importante, si no existe la key, te inicializa la key y el value y luego te
         * retorna este mismo
         * value inicializado
         */

    }

    static void sets() {
        /* Set */
        Set<String> fruits = new HashSet<>(Set.of("manzana", "pera"));
        var add = fruits.add("fresa");
        System.out.println(
                "el add(value) te agrega un elemento a tu HashSet,si el elemento ya esta agregado te retorna un false, sino un true: "
                        + add);
        System.out.println(fruits);

    }
}