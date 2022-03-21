import re


def compact_hanoi_graph(number_of_disks: int) -> str:
    if number_of_disks == 1:
        return " a \nb-c"
    else:
        top = compact_hanoi_graph(number_of_disks - 1)

        left = top.translate(top.maketrans("ac", "ca"))
        right = top.translate(top.maketrans("ab", "ba"))
        top = top.translate(top.maketrans("bc", "cb"))

        top = re.sub("(\w+)", lambda m: "a" + m.group(1), top)
        left = re.sub("(\w+)", lambda m: "b" + m.group(1), left)
        right = re.sub("(\w+)", lambda m: "c" + m.group(1), right)

        left_list = left.split("\n")
        right_list = right.split("\n")
        top_list = top.split("\n")

        bottom = [f"{x} {y}" for x, y in zip(left_list[:-1], right_list[:-1])] + [left_list[-1] + "-" + right_list[-1]]

        margin = len(top_list) * " "
        top_list = [margin + x + margin for x in top_list]
        return "\n".join(top_list + bottom)


def hanoi_graph(number_of_disks: int) -> str:
    compact_graph = compact_hanoi_graph(number_of_disks=number_of_disks)
    graph = compact_graph.replace("-", (2 + number_of_disks) * "-")
    graph = graph.replace(" ", (1 + number_of_disks) * " ")
    graph = re.sub('([\w|-]+)', lambda m: m.group(1) + " ", graph)

    graph_list = graph.split("\n")
    result = [graph_list[0]]
    for row in graph_list[1:]:
        vertical_row = make_first_vertical_edge_row(row, number_of_disks)
        for j in range(number_of_disks):
            result.append(vertical_row)
            vertical_row = vertical_row.replace(" /", "/ ").replace("\\ ", " \\")
        result.append(row)

    return "\n".join(result)


def make_first_vertical_edge_row(row: str, number_of_disks: int) -> str:
    result = row.replace("-", " ")
    margin = number_of_disks * " "
    result = re.sub("(\w+)( +)(\w+)",
                    lambda m: margin + "/" + (str(m.group(0)).count(" ") - 2) * " " + "\\" + margin,
                    result)
    return result
