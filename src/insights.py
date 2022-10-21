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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
