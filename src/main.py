# -*- coding: utf-8 -*-
import argparse
import sys

from pathlib import Path
from CalcRating import CalcRating
from CountSubjects import CountSubjects
from TextDataReader import TextDataReader
from TextDataReaderYaml import TextDataReaderYaml
from pprint import pprint


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    fileExtension = Path(path).suffix

    if fileExtension == '.txt':
        reader = TextDataReader()
        students = reader.read(path)
        print("Students: ", students)

        rating = CalcRating(students).calc()
        print("Rating: ", rating)
    else:
        reader = TextDataReaderYaml()
        students = reader.read(path)
        print("Students: ")
        pprint(students)

        rating = CountSubjects(students).calc()

        for i in rating:
            if rating.get(i) >= 3:
                print("Student: ", i)
                break
            else:
                print("No students")


if __name__ == "__main__":
    main()
