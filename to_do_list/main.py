from sqlmodel import SQLModel, create_engine, Field, select, Session

engine = create_engine('sqlite:///database.db', echo=False)

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    task: str = Field(max_length=80)

def main():
    SQLModel.metadata.create_all(engine)
    while True:
        user_input = input('Enter "A" to add task, "R" to read tasks. "U" to update tasks, "D" to delete tasks.')
        if user_input.upper() == 'A':
            task_to_add = input('Enter Task: ')
            add_task(task_to_add)
        elif user_input.upper() == 'R':
            print(read_tasks())
        elif user_input.upper() == 'U':
            print(update_task())
        elif user_input.upper() == 'D':
            print(delete_task())
        else:
            print('Enter A or R or U or D...')

def add_task(task_content):
    task = Task(task=task_content)
    with Session(engine) as session:
        session.add(task)
        session.commit()
    return 'Task Added'

def read_tasks():
    with Session(engine) as session:
        statement = select(Task.task)
        tasks = session.exec(statement).all()
    
    # for task in tasks:
    #     print(task.id, task.task)

    return "\n".join([f"{i}. {task}" for i, task in enumerate(tasks, 1)])


def update_task():
    print(read_tasks())
    task_num = int(input('Enter Task Number To Update: '))
    task_str = input('Enter the new task in place of previous one: ')


    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        db_task = tasks[task_num - 1]
        
        if not db_task:
            return "Task not found"
        
        db_task.task = task_str
        
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
    return f'Task {task_num} updated'

def delete_task():
    print(read_tasks())
    task_num = int(input('Enter Task Number To Delete: '))

    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        db_task = tasks[task_num - 1]
        
        if not db_task:
            return "Task not found"
        
        session.delete(db_task)
        session.commit()
        
    return f"Task {task_num} deleted successfully."



if __name__ == '__main__':
    main()


















