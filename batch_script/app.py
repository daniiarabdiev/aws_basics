import argparse


def main_script():
    parser = argparse.ArgumentParser()
    parser.add_argument('-message')
    args = parser.parse_args()

    target = f'Script done {args.message}'
    res = {'message': target}
    return res


main_script()

























