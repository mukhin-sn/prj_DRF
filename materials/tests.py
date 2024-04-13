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
        print('List lesson\n', response.json())
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(),
                          {
                              "count": 1,
                              "next": None,
                              "previous": None,
                              "results":
                                  [
                                      {
                                          "id": self.lesson_1.id,
                                          "link_to_video": None,
                                          "name": "lesson_name_1",
                                          "description": None,
                                          "preview": None,
                                          "course": self.course_1.id,
                                          "master": self.user_tst.id
                                      }
                                  ]
                          }
                          )

    def test_lesson_create(self):

        """Тест создания урока"""

        data = {
            "name": "lesson_name_2",
            "course": 1,
            "master": 1,
            "link_to_video": "youtube.com"
        }

        response = self.client.post(reverse('materials:lesson_create'), data=data)
        less_id = response.json()["id"]
        print('Create lesson\n', response.json())
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json(),
                          {
                              "id": less_id,
                              "link_to_video": "youtube.com",
                              "name": "lesson_name_2",
                              "description": None,
                              "preview": None,
                              "course": 1,
                              "master": 1
                          }
                          )

    def test_lesson_update(self):

        """Тест обновления записи урока"""

        data = {
            "link_to_video": "https://youtube.com",
            "description": "DeScRiPtIoN"
        }
        response = self.client.patch(f'/lesson/update/{self.lesson_1.id}/', data=data)
        print('Update lesson\n', response.json())
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(),
                          {
                              "id": self.lesson_1.id,
                              "link_to_video": "https://youtube.com",
                              "name": "lesson_name_1",
                              "description": "DeScRiPtIoN",
                              "preview": None,
                              "course": self.course_1.id,
                              "master": self.user_tst.id
                          }
                          )

    def test_lesson_retrieve(self):

        """Тест вывода записи одного урока"""

        response = self.client.get(f'/lesson/{self.lesson_1.id}/')
        print('Retrieve lesson\n', response.json())
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(),
                          {
                              "id": self.lesson_1.id,
                              "link_to_video": None,
                              "name": "lesson_name_1",
                              "description": None,
                              "preview": None,
                              "course": self.course_1.id,
                              "master": self.user_tst.id
                          }
                          )

    def test_lesson_destroy(self):

        """Тест удаления записи урока из базы"""

        response = self.client.delete(f'/lesson/delete/{self.lesson_1.id}/')
        print('Delete lesson\n', response.status_code)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
