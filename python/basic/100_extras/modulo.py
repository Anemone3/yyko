


"""
doc xd
"""
def some_thing(arg=None):
    print(f"""
          En python puedes ejecutar un script usando:
          py [archivo.py]
          Y esto es inicia un modulo que contiene esta siguientes propiedades

          __name__ -> {__name__}
          __doc__ -> {__doc__}
          __package__ -> {__package__}
          __loader__ -> {__loader__}
          __cached__ -> {__cached__}
          __file__ -> {__file__}
          __spec__ -> {__spec__}

          """)

    print(f"argumento que llego: {arg}")

#some_thing(1)

if __name__ == "__main__":
    print("""La razon por la que se hace esto es porque si lo importamos
    esto se va a ejecutar 2 veces, o la cantidad de veces que lo importemos""")

    import sys
    print("""incluso podemos pasar elementos al script si lo ejecutamos asi
        py [archivo.py] [argumento]
        """)
    some_thing(sys.argv[1])