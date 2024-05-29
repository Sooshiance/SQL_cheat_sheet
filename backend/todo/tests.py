from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from todo.models import ToDo


class ToDoTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.data1 = {"title":"Reading Books", "content":"Read the Python's books", "active":True,"status":1}
        self.data2 = {"title":'Review Books', "content":"Read the Rust's books", "active":True,"status":2}
        self.task1 = ToDo.objects.create(**self.data1)
        self.task2 = ToDo.objects.create(**self.data2)
        self.kwargs1 = {'pk':1}
        self.kwargs2 = {'pk':2}
        self.client = APIClient()
        self.all_tasks = reverse('all-tasks')
        self.one_task = reverse('one-task', kwargs=self.kwargs1)
        self.create_task = reverse('create-task')
        self.delete_task = reverse('delete-task', kwargs=self.kwargs1)
        self.update_task = reverse('update-task', kwargs=self.kwargs2)

    def test_getAllTasks(self):
        response = self.client.get(path=self.all_tasks)
        self.assertEqual(response.status_code, 200)

    def test_getSingleTask(self):
        response = self.client.get(path=self.one_task)
        self.assertEqual(response.status_code, 200)

    def test_createTask1(self):
        response = self.client.post(path=self.create_task, data={"title":'Review Books', "content":"Read the Rust's books","active":"true"}, format='json')
        self.assertEqual(response.status_code, 201)
    
    def test_deleteTask(self):
        response = self.client.delete(path=self.delete_task)
        self.assertEqual(response.status_code, 204)
    
    def test_updateTask(self):
        response = self.client.post(path=self.update_task, data={"title":"Books has been reviewed"})
        self.assertEqual(response.status_code, 204)
