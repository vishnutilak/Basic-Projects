import re

class Router:
    def __init__(self):
        self.routes = []  # (pattern, param_names, handler)

    def add(self, path_pattern, handler):
        # path_pattern like '/users/<id>'
        param_names = []
        regex = "^"
        for part in path_pattern.strip("/").split("/"):
            if part.startswith("<") and part.endswith(">"):
                name = part[1:-1]
                param_names.append(name)
                regex += r"/(?P<%s>[^/]+)" % name
            else:
                regex += "/" + re.escape(part)
        regex += "/?$"
        self.routes.append((re.compile(regex), param_names, handler))

    def route(self, path):
        for regex, params, handler in self.routes:
            m = regex.match(path)
            if m:
                return handler, m.groupdict()
        return None, None
