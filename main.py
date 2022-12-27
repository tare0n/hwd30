from Task import Task
from TodoList import TodoList

def task_test():
    print("Task testing: \n")
    todo_list = set()

    print("creating set from tasks: 'do hw', 'drink coffee', 'go jogging' and 'do hw'")

    todo_list.add(Task('do hw'))
    todo_list.add(Task('drink coffee'))
    todo_list.add(Task('go jogging'))
    todo_list.add(Task('do hw'))

    print("this set contains:\n")
    for item in todo_list:
        print(item)

    print("creating list of tasks with 'do hw', '', 'sleep', ''")

    todo_list = []

    todo_list.append(Task('do hw'))
    todo_list.append(Task(''))
    todo_list.append(Task('sleep'))
    todo_list.append(Task(''))

    print("list of non-empty tasks contains:")

    non_empty_tasks = [item for item in todo_list if item]
    print(non_empty_tasks)


def todo_test():
    print("\nTodoList testing:")
    todo_list = TodoList(2)
    todo_list[0] = Task("do hw")
    todo_list[1] = Task("drink coffee")
    print("after creating todo list with 'do hw' and 'drink coffee' task printing it with next()")
    print(next(todo_list))
    print(next(todo_list))
    print("and printing it with for loop")
    for item in todo_list:
        print(item)


def main():
    task_test()
    todo_test()


if __name__ == "__main__":
    main()
