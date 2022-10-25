from src.sorting import sort_by
from src.jobs import read


def test_sort_by_criteria():
    jobs = read('src/jobs.csv')

    job_list = []

    for job in jobs:
        if len(job_list) <= 5:
            job_list.append(
                (job["min_salary"]).isnumeric(),
                (job["max_salary"]).isnumeric(),
                job["date_posted"]
                )

    for criteria in ["min_salary", "max_salary", "date_posted"]:
        sort_by(job_list, criteria)

        if criteria == "min_salary":
            assert job_list[0][criteria] <= job_list[1][criteria]
        else:
            assert job_list[0][criteria] >= job_list[1][criteria]
