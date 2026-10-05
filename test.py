import ast
import importlib.util
import re
import sys
from pathlib import Path
from types import ModuleType
from typing import Any


_PYTHON_LEETCODE_ROOT = Path(__file__).resolve().parent / "python" / "leetcode"


class RunnerError(Exception):
    pass


def _parse_argument(value: str) -> Any:
    try:
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value


def _load_exercise(problem: str) -> ModuleType:
    if not re.fullmatch(r"[A-Za-z_]\w*", problem):
        raise RunnerError(f"Nombre de ejercicio invalido: {problem!r}")

    matches = list(_PYTHON_LEETCODE_ROOT.rglob(f"{problem}.py"))
    if not matches:
        raise RunnerError(f"No se encontro el ejercicio de Python {problem!r}")
    if len(matches) > 1:
        paths = ", ".join(str(path.relative_to(_PYTHON_LEETCODE_ROOT)) for path in matches)
        raise RunnerError(f"El nombre {problem!r} es ambiguo; coincidencias: {paths}")

    path = matches[0]
    spec = importlib.util.spec_from_file_location(f"leetcode_{problem}", path)
    if spec is None or spec.loader is None:
        raise RunnerError(f"No se pudo cargar el ejercicio: {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _method_for(solution: object, problem: str):
    method_name = "".join(part.capitalize() for part in problem.split("_"))
    method_name = method_name[:1].lower() + method_name[1:]
    method = getattr(solution, method_name, None)
    if callable(method):
        return method

    public_methods = [
        getattr(solution, name)
        for name in dir(solution)
        if not name.startswith("_") and callable(getattr(solution, name))
    ]
    if len(public_methods) == 1:
        return public_methods[0]
    raise RunnerError(
        f"No se encontro un metodo para {problem!r} en la clase Solution"
    )


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    language = "python"
    if args and args[0] == "--language":
        if len(args) < 2:
            print("Error: falta el lenguaje despues de --language", file=sys.stderr)
            return 2
        language, *args = args[1:]
    elif args and args[0] == "python":
        args.pop(0)

    if language != "python":
        print(f"Error: por ahora solo se soporta Python (recibido: {language})", file=sys.stderr)
        return 2

    if not args:
        print(
            "Uso: python test.py [--language python] <ejercicio> [argumentos...]\n"
            "Ejemplo: python test.py contains_duplicates \"[1, 2, 3, 3]\"",
            file=sys.stderr,
        )
        return 2

    problem, *raw_arguments = args

    try:
        module = _load_exercise(problem)
        solution_class = getattr(module, "Solution", None)
        if solution_class is None:
            raise RunnerError(f"{problem!r} no define una clase Solution")

        solution = solution_class()
        method = _method_for(solution, problem)
        result = method(*(_parse_argument(value) for value in raw_arguments))
    except RunnerError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print("Result: ", result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
