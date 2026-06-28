
def print_menu():
    print('\nToDo List Menu:')
    print('1. View Active Tasks')
    print('2. View Completed Tasks')
    print('3. Add a Task')
    print('4. Mark Task as Completed')
    print('5. Remove Task')
    print('6. Exit')

def get_choice():
    while True:
        try:
            choice = int(input('Enter your choice: '))
            if 1 <= choice <= 6:
                return choice
            else:
                print('Invalid choice. Please enter a number between 1 and 6.')
        except ValueError:
            print('Invalid input. Please enter a number.')

def add_task(tasks):
    while True:
        task_name = input('Enter task name: ').strip()
        if len(task_name) != 0:
            new_task = {'name': task_name, 'completed': False}
            tasks.append(new_task)
            break
        else:
            print('Task name cannot be empty.')
            break
            
def display_tasks(tasks, show_completed):
    count = 0
    for task in tasks:
        if task['completed'] == show_completed:
            count += 1
            print(f'{count}. {task["name"]}')
            
    if count == 0:
        if show_completed:
            print('No completed tasks in the list.')
        else:
            print('No active tasks in the list.')
            
    return count

def mark_task_completed(tasks):
    
    if len(tasks) == 0:
        print('No tasks are remaining')
        return

    # Show all tasks with their current status
    for index, task in enumerate(tasks, start=1):
        status = '[Done]' if task['completed'] else '[Active]'
        print(f'{index}. {status} {task["name"]}')

    while True:
        try:
            task_number = int(input('Enter the task number to mark completed: '))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]['completed'] = True
                print('Task marked as completed')
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid task number')


def remove_task(tasks):
    if len(tasks) == 0:
        print('No tasks to remove.')
        return

    # Show all tasks with their current status
    for index, task in enumerate(tasks, start=1):
        status = '[Done]' if task['completed'] else '[Active]'
        print(f'{index}. {status} {task["name"]}')

    while True:
        try:
            task_number = int(input('Enter the task number to remove permanently: '))
            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                print(f'Permanently removed "{removed["name"]}"')
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid task number')

def main():
    tasks = []
    while True:
        print_menu()
        choice = get_choice()
        print(f'Entered choice: {choice}')
        if choice == 1:
            print('\n--- Active Tasks ---')
            display_tasks(tasks, show_completed=False)
        if choice == 2:
            print('\n--- Completed Tasks ---')
            display_tasks(tasks, show_completed=True)
        if choice == 3:
            add_task(tasks)
        if choice == 4:
            mark_task_completed(tasks)
        if choice == 5:
            remove_task(tasks)
        if choice == 6:
            print('Good By')   
            break
        

if __name__ == "__main__":
    main()