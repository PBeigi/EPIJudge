from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()
    unadjusted_salaries_sum = 0
    n = len(current_salaries)
    for i, cur_salary in enumerate(current_salaries):
        adjusted_salary_count = n - i
        adjusted_salaries_sum = adjusted_salary_count * cur_salary
        if unadjusted_salaries_sum + adjusted_salaries_sum >= target_payroll:
            return (target_payroll - unadjusted_salaries_sum) / adjusted_salary_count
        unadjusted_salaries_sum+=cur_salary
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
