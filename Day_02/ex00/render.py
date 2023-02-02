import settings as cv_vars
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()

    if not sys.argv[1].endswith(".template"):
        sys.exit()

    template_path = sys.argv[1]

    with open(template_path) as template_file:
        contents = template_file.read()
        contents = contents.replace("{name}", str(cv_vars.name))
        contents = contents.replace("{surname}", str(cv_vars.surname))
        contents = contents.replace("{age}", str(cv_vars.age))
        contents = contents.replace("{profession}", str(cv_vars.profession))

        output_file = open("cv.html", "w")
        output_file.write(contents)
        output_file.close()
