def domain_name(url: str):
    def format_www(url: str):
        if url.startswith("www."):
            val = url.split("www.")
            val = [l for l in val if l != ""]
            val = val[0].split(".")
            return val[0]
        return url

    if url.startswith("http") or url.startswith("https"):
        rest = url.split("://")
        print(rest)
        rest = format_www(url=rest[1])
        if "." in rest:
            return rest.split(".")[0]
        return rest
    if url.startswith("www"):
        return format_www(url)
    return url.split(".")[0]


print(domain_name("www.xakep.ru"))
