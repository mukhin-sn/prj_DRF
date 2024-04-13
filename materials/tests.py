from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonAPITestCase(APITestCase):

    def setUp(self):
        # Создаем экземпляр класса APIClient
        self.client = APIClient()

        # Создаем юзера
        self.user_tst = User.objects.create(email="test@test.com", first_name='user_tst', password='user_tst')
        self.user_tst.set_password('user_tst')
        self.user_tst.save()
        self.client.force_authenticate(user=self.user_tst)

        # Создаем объект модели Course
        self.course_1 = Course.objects.create(
            name="course_name_1"
        )

        # Создаем объект модели Lesson
        self.lesson_1 = Lesson.objects.create(
            name="lesson_name_1",
            course=self.course_1,
            master=self.user_tst
        )

        # self.lesson_2 = Lesson.objects.create(
        #     name="lesson_name_2",
        #     course=self.course_1,
        #     master = self.user_tst
        # )

    # Тесты
    def test_lesson_list(self):
        """Тест вывода списка уроков"""
        response = self.client.get(reverse('materials:lessons'))
        # response = self.client.get('/lesson/')
        print('List lessons\n', response.json())
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(),
                          {
                              'count': response.json()["count"],
                              'next': None,
                              'previous': None,
                              'results':
                                  [
                                      {
                                          'id': response.json()["results"][0]["id"],
                                          'link_to_video': None,
                                          'name': 'lesson_name_1',
                                          'description': None,
                                          'preview': None,
                                          'course': response.json()["results"][0]["course"],
                                          'master': response.json()["results"][0]["master"]
                                      }
                                  ]
                          }
                          )

    def test_lesson_create(self):
        """Тест создания урока"""
        # print(self.course_1, self.user_tst)
        data = {
            "name": "lesson_name_2",
            "course": 1,
            "master": 1,
            "link_to_video": "youtube.com"
        }

        response = self.client.post(reverse('materials:lesson_create'), data=data)
        print('Create lesson\n', response.json())
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_update(self):
        """Тест обновления записи урока"""
        data = {
            "link_to_video": "https://youtube.com"
        }
        print(self.client.get('/lesson/1/').json())
        response = self.client.patch('/lesson/update/1/', data=data)
        print('Update lesson\n', response.json())
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_lesson_retrieve(self):
        """Тест вывода записи одного урока"""
        response = self.client.get('/lesson/1/')
        print('Retrieve lesson\n', response.json())
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_lesson_destroy(self):
        """Тест удаления записи урока из базы"""
        print(self.client.get('/lesson/1/').json())
        response = self.client.delete('/lesson/delete/1/')
        print('Delete lesson\n', response.status_code)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
