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
        .show {
            width: 50px;
            height: 50px;
            border: solid;
        }
        .hide {
            width: 50px;
            height: 50px;
            border: none;
        }
        ul {
            list-style: none;
        }
    </style>
</head>
<body>
    <h1 style="color: blue">Hello World!</h1>
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
                        <h4>name</h4>
                        <ul>
                            <li>''' + current_element["number"] + '''</li>
                            <li>''' + current_element["small"] + '''</li>
                            <li>''' + current_element["molar"] + '''</li>
                        </ul>
                    </td>
                ''')


def get_object_from_line(batata):
    print("dentro da object:", batata)
    if batata == "":
        print("entrou no if")
        return {}
    line_read = batata.strip().split('=')[1].strip()

    # Split the string into a list of key-value pairs
    key_value_pairs = line_read.split(', ')

    # Create an empty dictionary
    data_dict = {}

    # Loop through each key-value pair and add it to the dictionary
    for key_value in key_value_pairs:
        key, value = key_value.split(':')
        data_dict[key] = value.strip()

    return data_dict

def write_table(output_file, input_file):
    current_element = get_object_from_line(input_file.readline())
    print("current element: ", current_element)
    pos_int = int(current_element["position"])

    for tr in range(7):
        open_tr_tag(output_file)
        for td in range(18):
            if pos_int == td:
                # escreve a tag com os elementos
                write_show(output_file, current_element)
                # lança um outro readline
                print("td:", td, "curr el:", current_element)
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
