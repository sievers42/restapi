
import logging
from datetime import datetime
from flask import make_response, abort

logging.basicConfig(filename='todo.log',level=logging.INFO)
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
TODO = {
    "Clean": {
        "title": "Clean",
        "task": "Clean the kitchen",
        "timestamp": get_timestamp()
    },
    "Groceries": {
        "title": "Description",
        "task": "Buy groceries",
        "timestamp": get_timestamp()
    },
    "Dog": {
        "title": "Dog",
        "task": "Walk the dog",
        "timestamp": get_timestamp()
    }
}


def read_all():

    # Create the list of tasks
    logging.info('%s: Reading all tasks', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")))
    return [TODO[key] for key in sorted(TODO.keys())]

def delete_all():

        # Delete list of tasks
        logging.info('%s: Deleting all tasks', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")))
        del TODO
        logging.info('%s: All tasks deleted', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")))
        return 200


def read_one(title):

    # Does the title exist in TODO?
    logging.info('%s: Attempting to read %s', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), title)
    if title in TODO:
        tasktodo = TODO.get(title)

    # otherwise, not found
    else:
        logging.info('%s: %s not found', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), title)
        abort(
            404, "TODO with title {title} not found".format(title=title)
        )
    logging.info('%s: %s found', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), title)
    return tasktodo


def create(todo):
    logging.info('%s: Attempting to create %s', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), todo.get("title", None))
    title = todo.get("title", None)
    task = todo.get("task", None)

    # Does task exist already?
    if title not in TODO and title is not None:
        TODO[title] = {
            "title": title,
            "task": task,
            "timestamp": get_timestamp(),
        }
        logging.info('%s: %s created', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), todo.get("title", None))
        return make_response(
            "{title} successfully created".format(title=title), 201
        )

    # Otherwise, it already exist,  error
    else:
        logging.info('%s: %s already exists', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), todo.get("title", None))
        abort(
            406,
            "task with title {title} already exists".format(title=title),
        )


def update(title, todo):

    logging.info('%s: Attempting to update %s', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), title)
    # Does task exist?
    if title in TODO:
        TODO[title]["task"] = todo.get("task")
        TODO[title]["timestamp"] = get_timestamp()
        logging.info('%s: %s updated', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), title)
        return TODO[title]

    # otherwise, error
    else:
        logging.info('%s: %s not found', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), title)
        abort(
            404, "Task with title {title} not found".format(title=title)
        )


def delete(title):

    logging.info('%s: Attempting to delete %s', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), title)
    # Does the task to delete exist?
    if title in TODO:
        del TODO[title]
        logging.info('%s: %s deleted', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), title)
        return make_response(
            "{title} successfully deleted".format(title=title), 200
        )

    # Otherwise, task to delete not found
    else:
        logging.info('%s: %s not found', datetime.now().strftime(("%Y-%m-%d %H:%M:%S")), title)
        abort(
            404, "task with title {title} not found".format(title=title)
)


