# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    periodic_table.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ewolfghe <ewolfghe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/01 13:01:00 by ewolfghe          #+#    #+#              #
#    Updated: 2023/02/01 15:55:14 by ewolfghe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

alkali_metals = ["Li", "Na", "K", "Rb", "Cs", "Fr"]
alkaline_earth_metals = ["Be", "Mg", "Ca", "Sr", "Ba", "Ra"]
transition_metals = ["Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh",
                     "Pd", "Ag", "Cd", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn"]
post_transition_metals = ["Al", "Ga", "In", "Tl",
                          "Sn", "Pb", "Bi", "Uut", "Fl", "Uup", "Lv"]
metalloids = ["B", "Si", "Ge", "As", "Sb", "Te", "Po"]
nonmetals = ["H", "C", "N", "O", "P", "S", "Se"]
halogens = ["F", "Cl", "Br", "I", "At", "Ts", "Uus"]
noble_gases = ["He", "Ne", "Ar", "Kr", "Xe", "Rn", "Uuo"]


def write_header(output_file):
    output_file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Periodic Table</title>
    <style>
        body {
            font-size: 0.7em;
        }
        .show, .hide {
            width: 100px;
            height: 10px;
        }
        .show {
            border: solid 1px;
        }
        .hide {
            border: none;
        }
        #table-title {
            text-align: center;
            font-size: xxx-large;
        }
        ul {
            padding: 0;
            list-style-type: none;
        }
        .element-number {
            padding-left: 10px;
        }
        ul .other{
            text-align: center;
        }
        h1, h4 {
            margin: 7px;
        }
        .alkali_metals {
            background-color: #f1c35a;
        }
        .alkaline_earth_metals {
            background-color: #ebe555;
        }
        .transition_metals {
            background-color: #ef9dab;
        }
        .post_transition_metals {
            background-color: #a7cad2;
        }
        .metalloids {
            background-color: #7ac8b6;
        }
        .nonmetals {
            background-color: #a9db5f;
        }
        .noble_gases {
            background-color: #7baedf;
        }
        .halogens {
            background-color: #b4e2f1;
        }
    </style>
</head>
<body>
    <h1 id="table-title">Periodic Table</h1>
    <table>
''')


def open_tr_tag(output_file):
    output_file.write('''
            <tr>
    ''')


def close_tr_tag(output_file):
    output_file.write('''
        </tr>
    ''')


def write_bg_color(small):
    if small in alkali_metals:
        return ("alkali_metals")
    elif small in alkaline_earth_metals:
        return ("alkaline_earth_metals")
    elif small in transition_metals:
        return ("transition_metals")
    elif small in post_transition_metals:
        return ("post_transition_metals")
    elif small in metalloids:
        return ("metalloids")
    elif small in nonmetals:
        return ("nonmetals")
    elif small in noble_gases:
        return ("noble_gases")
    elif small in halogens:
        return ("halogens")
    else:
        return ("unknown")


def write_show(output_file, current_element):
    output_file.write('''
                    <td class="show ''' + write_bg_color(current_element["small"]) + '''">
                        <ul>
                            <li class="element-number">''' + current_element["number"] + '''</li>
                            <li class="other"><h1>''' + current_element["small"] + '''</h1></li>
                            <li class="other"><h4>''' + current_element["name"] + '''</h4></li>
                            <li class="other">''' + current_element["molar"] + '''</li>
                        </ul>
                    </td>
                ''')


def get_object_from_line(batata):
    data_dict = {}

    if batata == "":
        return {}

    pamonha = batata.strip().split('=')

    data_dict["name"] = pamonha[0]

    line_read = pamonha[1].strip()

    # Split the string into a list of key-value pairs
    key_value_pairs = line_read.split(', ')

    # Create an empty dictionary

    # Loop through each key-value pair and add it to the dictionary
    for key_value in key_value_pairs:
        key, value = key_value.split(':')
        data_dict[key] = value.strip()

    return data_dict


def write_table(output_file, input_file):
    current_element = get_object_from_line(input_file.readline())
    pos_int = int(current_element["position"])

    for tr in range(7):
        open_tr_tag(output_file)
        for td in range(18):
            if pos_int == td:
                # escreve a tag com os elementos
                write_show(output_file, current_element)
                # lança um outro readline
                current_element = get_object_from_line(input_file.readline())
                if current_element != {}:
                    pos_int = int(current_element["position"])
            else:
                output_file.write('''
                    <td class="hide"></td>
                ''')
        close_tr_tag(output_file)


def write_footer(file):
    file.write('''
            </table>
        </body>
    </html>
    ''')


def periodic_table():
    # Creating the HTML file
    output_file = open("periodic_table.html", "w")
    write_header(output_file)

    # Open input file with periodic table information
    input_file = open("periodic_table.txt", "r")
    write_table(output_file, input_file)

    write_footer(output_file)

    output_file.close()
    input_file.close()


if __name__ == "__main__":
    periodic_table()
