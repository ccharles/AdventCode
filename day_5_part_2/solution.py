from intcode_computer import IntcodeComputer, parse_program

INPUT_FILE = './inputs/task_5_part_2_input.txt'


def solution():
    from pathlib import Path
    input_file = Path(INPUT_FILE)
    # parse the sequence of commands and replace two elements with values
    # according to the task
    num_sequence = parse_program(input_file)
    computer = IntcodeComputer(program=num_sequence)
    # set the input value that we want to pass to the Input command
    computer.send_input_data(5)
    computer.run_program()
    return computer.output_buffer.value


if __name__ == '__main__':
    import os
    os.chdir('..')

    print(solution())
