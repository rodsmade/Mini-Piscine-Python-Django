import sys

def get_template_path():
    if len(sys.argv) != 2:
        print("Error. Pass in only one argument, e.g.: `python3 render.py myCV.template`")
        sys.exit()

    if not sys.argv[1].endswith(".template"):
        print("Error. File must end in `.template`, e.g.: `myCV.template`")
        sys.exit()

    return sys.argv[1]

if __name__ == "__main__":
    template_path = get_template_path()
    template_contents = open(template_path, 'r').read()

    settings_contents = open("settings.py", "r")
    setting_variables = {}
    for line in settings_contents:
        if line[0] != '#':
            key_value = line.split(" = ")
            template_contents = template_contents.replace("{" + key_value[0] + "}", key_value[1].strip('"\n'))

    output_file = open(sys.argv[1].split('.')[0] + ".html", "w")
    output_file.write(template_contents)
    output_file.close()
