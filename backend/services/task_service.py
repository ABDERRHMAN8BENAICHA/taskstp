from database import tasks_collection
from bson import ObjectId

def create_task(task):
    task_dict = task.dict()
    result = tasks_collection.insert_one(task_dict)
    return str(result.inserted_id)


def get_tasks(user_id: int):
    tasks = list(tasks_collection.find({"user_id": user_id}))

    for t in tasks:
        t["_id"] = str(t["_id"])

    return tasks


def delete_task(task_id):
    result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return {"deleted_count": result.deleted_count}