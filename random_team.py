import random


def stringify(L: list[list[str]]) -> str:
    output = ''
    for pair in L:
        output += ' - '.join(pair)
        output += '\n'

    return output


def get_random_pairs(students: list, students_in_group: int = 2) -> str:
    """Divide the given list of students into the given number of groups. 

    Args:
        students (list): List of students
        students_in_group (int, optional): Number of students per group. Defaults to 2.

    Returns:
        str: Students divided into groups
    """

    random.shuffle(students)
    number_of_groups = len(students) // students_in_group - 1
    output = []
    group = 0

    while group <= number_of_groups:
        if group != number_of_groups:
            output.append(
                students[group * students_in_group:(group * students_in_group) + students_in_group])
        else:
            output.append(students[group * students_in_group:])
        group += 1

    return stringify(output)


if __name__ == "__main__":
    students = ['Alexander A.', 'Anthony B.', 'Bhagirath B.', 'Robert C.', 'Louis C.',
                'Ashley C.', 'Grace C.', 'Jae C.', 'Samuel C.', 'Sian C.', 'Kim D.', 'Nick D.',
                'Amber F.', 'Mason F.', 'Brandon G.', 'Sean H.', 'Ben H.', 'Matthew H.',
                'Logan J.', 'Nebiyu K.', 'Alan M.', 'Audrena S.']

    print(get_random_pairs(students))
