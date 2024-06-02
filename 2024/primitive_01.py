"""
(function) def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False
) -> None

print("안녕","하세요")
print("안녕","하세요", end='.')
print("안녕","하세요", sep='-')
"""