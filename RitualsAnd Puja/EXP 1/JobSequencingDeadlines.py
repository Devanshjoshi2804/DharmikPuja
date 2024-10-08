def job_sequencing(job_list):
    job_list.sort(key=lambda x: x[2], reverse=True)  # Sort jobs based on profit (deadline)

    max_deadline = max(job[1] for job in job_list)
    schedule = [None] * max_deadline

    total_profit = 0

    for job in job_list:
        deadline = job[1]
        while deadline > 0:
            if schedule[deadline - 1] is None:
                schedule[deadline - 1] = job[0]
                total_profit += job[2]
                break
            deadline -= 1

    return total_profit, [job for job in schedule if job is not None]

def main():
    # Job format: (job_id, deadline, profit)
    job_list = [(1, 2, 100), (2, 1, 50), (3, 2, 200), (4, 1, 75), (5, 3, 300)]
    max_profit, schedule = job_sequencing(job_list)
    print("Maximum Profit:", max_profit)
    print("Job Schedule:", schedule)

if __name__ == "__main__":
    main()
