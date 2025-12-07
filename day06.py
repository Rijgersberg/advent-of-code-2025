from collections import defaultdict

from aoc import get_input


def parse1(lines):
    problems = defaultdict(list)
    for line in lines[:-1]:
        for i, num in enumerate(line.split()):
            problems[i].append(num)
    operators = [operator.strip() for operator in lines[-1].split()]
    
    return [operators[index].join(operands) for index, operands in problems.items()]


def parse2(lines):
    index_of_operands = [i for i, char in enumerate(lines[-1]) if char != ' '] + [len(lines[0])+1]

    problems = []
    for start, end in zip(index_of_operands[:-1], index_of_operands[1:]):
        operator = lines[-1][start]
        operands_text = [line[start:end-1] for line in lines[:-1]]

        operands = []
        for p in range(len(operands_text[0])-1, -1, -1):
            num = ''.join(human_num[p] for human_num in operands_text)
            operands.append(num)
        
        problems.append(operator.join(operands))        
    return problems


lines = get_input(day=6, as_list=False).splitlines()

problems = parse1(lines)
print(sum(eval(problem) for problem in problems))

problems = parse2(lines)
print(sum(eval(problem) for problem in problems))
