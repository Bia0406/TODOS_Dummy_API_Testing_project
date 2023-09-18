import requests


class TodosDummyRequests:
    BASE_URL = "https://dummyjson.com/todos"

    def get_all_todos(self):
        url = self.BASE_URL
        resp = requests.get(url=url)
        return resp

    def get_single_todo_by_id(self, todo_id):
        url = f"{self.BASE_URL}/{todo_id}"
        resp = requests.get(url=url)
        return resp

    def get_todo_by_random(self):
        url = f"{self.BASE_URL}/random"
        resp = requests.get(url=url)
        return resp

    def get_limit_and_skip_todos(self, limit=None, skip=None):
        url = self.BASE_URL

        request_params = {}
        if limit is not None:
            request_params.update({"limit": limit})
        if skip is not None:
            request_params.update({"skip": skip})

        resp = requests.get(url=url, params=request_params)
        return resp

    def get_all_todos_by_user_id(self, user_id):
        url = f"{self.BASE_URL}/user/{user_id}"
        resp = requests.get(url=url)
        return resp

    def add_new_todo(self, todo, completed, userId):
        url = f"{self.BASE_URL}/add"
        request_body = {
            "todo": todo,
            "completed": completed,
            "userId": userId
        }
        resp = requests.post(url=url, json=request_body)
        return resp

    def update_todo(self, todo_id, completed):
        url = f"{self.BASE_URL}/{todo_id}"
        request_body = {
             "completed": completed
        }
        resp = requests.patch(url=url, json=request_body)
        return resp

    def delete_todo(self, todo_id):
        url = f"{self.BASE_URL}/{todo_id}"
        resp = requests.delete(url=url)
        return resp


obj = TodosDummyRequests()
response1 = obj.get_all_todos()
print(response1.status_code)
print(response1.json())

