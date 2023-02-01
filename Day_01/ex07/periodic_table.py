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
    </style>
</head>
<body>
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

def write_show(output_file, current_element):
    output_file.write('''
                    <td class="show">
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
    output_file = open("demo.html", "w")
    write_header(output_file)

    # Open input file with periodic table information
    input_file = open("periodic_table.txt", "r")
    write_table(output_file, input_file)

    write_footer(output_file)

    output_file.close()
    input_file.close()

if __name__ == "__main__":
    periodic_table()
