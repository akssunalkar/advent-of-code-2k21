from utils import open_file
from pathlib import Path
import math

HEX_TO_BINARY = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def literal_func(packet_body: str, multiple_groups: bool):
    last_group_indicator = False
    idx = 0
    val = ""
    if multiple_groups:
        while True:
            if last_group_indicator:
                break
            group_indicator = packet_body[0]
            if group_indicator == "0":
                last_group_indicator = True

            val += packet_body[1:5]
            packet_body = packet_body[5:]
            idx += 5
    else:
        val += packet_body[1:5]
        packet_body = packet_body[5:]
    return int(val, 2), packet_body


def get_packet_header_and_config(packet: str):
    version = int(packet[:3], 2)
    type_id = packet[3:6]
    if int(type_id, 2) == 4:
        type_id_str = "literal"
        indicator = bool(int(packet[6], 2))
    else:
        type_id_str = int(type_id, 2)
        indicator = bool(int(packet[6], 2))
    packet_rem = packet[6:]
    return version, type_id_str, indicator, packet_rem


def data_parser(message_string: str, version_sum: int):

    if len(message_string) > 6:
        version, type_id_str, indicator, message_string = get_packet_header_and_config(
            packet=message_string
        )
        version_sum += version
        if type_id_str == "literal":
            multiple_groups = indicator
            literal_value, message_string = literal_func(
                packet_body=message_string, multiple_groups=multiple_groups
            )
        else:
            message_string = message_string[1:]
            if not indicator:
                total_bit_length = int(message_string[:15], 2)
                sample_string = message_string[15 : 15 + total_bit_length]
                message_string = message_string[15 + total_bit_length :]
                while len(sample_string) > 6:
                    sample_string, version_sum = data_parser(
                        message_string=sample_string, version_sum=version_sum
                    )
            else:
                num_packets = int(message_string[:11], 2)
                message_string = message_string[11:]
                for i in range(num_packets):
                    message_string, version_sum = data_parser(
                        message_string=message_string, version_sum=version_sum
                    )
    return message_string, version_sum


# Part 1
# mess = "A0016C880162017C3686B18A3D4780"
message = open_file(file_path=Path("problem_16/pr_16.txt"), as_list_values=False)

m_bits = ""
for m in message:
    m_bits += HEX_TO_BINARY[m]

m, v = data_parser(m_bits, version_sum=0)
print(v)

operations = [
    sum,
    math.prod,
    min,
    max,
    lambda ls: ls[0],  # literal
    lambda ls: 1 if ls[0] > ls[1] else 0,  # gt
    lambda ls: 1 if ls[0] < ls[1] else 0,  # lt
    lambda ls: 1 if ls[0] == ls[1] else 0,  # eq
]


def data_parser_part2(message_string: str):
    if len(message_string) > 6:
        version, type_id_str, indicator, message_string = get_packet_header_and_config(
            packet=message_string
        )
        if type_id_str == "literal":
            value_list = []
            type_id_str = 4
            multiple_groups = indicator
            literal_value, message_string = literal_func(
                packet_body=message_string, multiple_groups=multiple_groups
            )
            value_list.append(literal_value)
        else:
            value_list = []
            message_string = message_string[1:]
            if not indicator:
                total_bit_length = int(message_string[:15], 2)
                sample_string = message_string[15 : 15 + total_bit_length]
                message_string = message_string[15 + total_bit_length :]
                while len(sample_string) > 6:
                    sample_string, val = data_parser_part2(message_string=sample_string)
                    value_list.append(val)
            else:
                num_packets = int(message_string[:11], 2)
                message_string = message_string[11:]
                for i in range(num_packets):
                    message_string, val = data_parser_part2(
                        message_string=message_string
                    )
                    value_list.append(val)

        val = operations[type_id_str](value_list)
    return message_string, val


# message="9C005AC2F8F0"
message = open_file(file_path=Path("problem_16/pr_16.txt"), as_list_values=False)
# print(message)
m_bits = ""
for m in message:
    m_bits += HEX_TO_BINARY[m]

m, val = data_parser_part2(m_bits)
print(val)
