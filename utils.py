from os import environ

def getenv(env, default_value):
    if env in environ:
        return environ[env]
    else:
        return default_value

def clean_carriage_return(lines):
    formatted_lines = []
    for line in lines:
        formatted_lines.append(line.replace('\n',''))
    return formatted_lines