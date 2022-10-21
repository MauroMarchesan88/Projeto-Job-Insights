from src.jobs import read


def get_unique_job_types(path):

    jobs = read(path)

    job_types = []

    for job in jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):

    list_of_jobs = []

    for job in jobs:
        if job["job_type"] == job_type and job["job_type"] not in list_of_jobs:
            list_of_jobs.append(job)

    return list_of_jobs


def get_unique_industries(path):

    jobs = read(path)

    industries_types = []

    for job in jobs:
        if job["industry"] not in industries_types and job["industry"]:
            industries_types.append(job["industry"])

    return industries_types


def filter_by_industry(jobs, industry):
    list_industr = []

    for job in jobs:
        if job["industry"] == industry and job["industry"] not in list_industr:
            list_industr.append(job)

    return list_industr


def get_max_salary(path):

    jobs = read(path)

    salaries = []

    for job in jobs:
        if job["max_salary"] not in salaries and job["max_salary"].isnumeric():
            salaries.append(int(job["max_salary"]))

    return max(salaries)


def get_min_salary(path):

    jobs = read(path)

    salaries = []

    for job in jobs:
        if job["min_salary"] not in salaries and job["min_salary"].isnumeric():
            salaries.append(int(job["min_salary"]))

    return min(salaries)


def matches_salary_range(job, salary):

    min_salary = job.get('min_salary')
    max_salary = job.get('max_salary')

    if not isinstance(salary, int):
        raise ValueError('Salary must be a positive number.')

    if not isinstance(min_salary, int):
        raise ValueError('Job min salary must be a number.')

    if not isinstance(max_salary, int):
        raise ValueError('Job min salary must be a number.')

    if (max_salary < min_salary):
        raise ValueError('Job min salary must be lower than max.')

    return min_salary <= salary <= max_salary


def filter_by_salary_range(jobs, salary):

    list_of_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_of_jobs.append(job)
        except ValueError as ve:
            print(ve)

    return list_of_jobs
