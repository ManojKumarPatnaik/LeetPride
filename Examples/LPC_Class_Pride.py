from LeetPrideCore import *


class Pride:
    def __init__(self, pride: str):
        self.love = pride

    def loving(self, pride: str = '!!!') -> str:
        return 'LGBTQ Lover ' + self.love + pride


def generate_tests():
    tests_unified = []
    #  \/\/\/\/\/\/\/\/\/\/ Set tests in these sections \/\/\/\/\/\/\/\/\/\/ #
    tests = (['Pride', 'loving', ],
             ['forever !',
              None,
              ])
    expected_test_results = [True, 'LGBTQ Lover forever !!!!', ]
    #  ^^^^^^^^^^^^^^^^^^^^ Set tests in these sections ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #

    tests_unified += list(zip(tests[0], tests[1], expected_test_results))
    return tests_unified


def main() -> Optional[int] | None:
    tests_unified = generate_tests()
    lpc = LeetPrideCore()
    lpc.solution_hash_display(tests_unified=tests_unified)
    any_fail = lpc.run_tests(tests_unified)
    return completion_display(any_fail)


if __name__ == '__main__':  # most of this relevant only for large recursion situations or concurrency needs
    exit(main())
