from background_task import background

@background(schedule = 60)
def do_task(num_task):
    # You can add your task in here
    task_list = []
    for i in range(num_task):
        item = 'LONG RUNNING PROCESS #' + str(i)
        task_list.append(item)
    print(task_list)