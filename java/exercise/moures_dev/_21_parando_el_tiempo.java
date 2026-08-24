/*
    Crea una función que sume 2 números y retorne su resultado pasados
    unos segundos.
    - Recibirá por parámetros los 2 números a sumar y los segundos que
    debe tardar en finalizar su ejecución.
    - Si el lenguaje lo soporta, deberá retornar el resultado de forma
    asíncrona, es decir, sin detener la ejecución del programa principal.
    Se podría ejecutar varias veces al mismo tiempo.
*/

import java.util.concurrent.CompletableFuture;

public class _21_parando_el_tiempo {

    public static CompletableFuture<Integer> delayedSum(int a, int b, int seconds) {

        return CompletableFuture.completedFuture(0);
    }

    public static void main(String[] args) {

    }
}
