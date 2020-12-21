import random


def stringify(L: list[list[str]]) -> str:
    output = ''
    for pair in L:
        output += ' - '.join(pair) + '\n'

    return output


def get_random_pairs(students: list, students_per_group: int = 2) -> str:
    """Divide the given list of students into groups where each group contains the given number of students. All extra students will be added to the last group. 

    Args:
        students (list): List of students
        students_per_group (int, optional): Number of students per group. Defaults to 2.

    Returns:
        str: Students divided into groups
    """

    random.shuffle(students)
    number_of_groups = len(students) // students_per_group - 1
    output = []
    group = 0

    while group <= number_of_groups:
        if group != number_of_groups:
            output.append(
                students[group * students_per_group:(group * students_per_group) + students_per_group])
        else:
            output.append(students[group * students_per_group:])
        group += 1

    return stringify(output)


if __name__ == "__main__":
    students = ['Alexander A.', 'Anthony B.', 'Bhagirath B.', 'Robert C.', 'Louis C.',
                'Ashley C.', 'Grace C.', 'Jae C.', 'Samuel C.', 'Sian C.', 'Kim D.', 'Nick D.',
                'Amber F.', 'Mason F.', 'Brandon G.', 'Sean H.', 'Ben H.', 'Matthew H.',
                'Logan J.', 'Nebiyu K.', 'Alan M.', 'Audrena S.']

    print(get_random_pairs(students))
