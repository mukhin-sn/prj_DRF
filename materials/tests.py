from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonAPITestCase(APITestCase):

    def setUp(self):

        # Создаем экземпляр класса APIClient
        self.client = APIClient()

        # Создаем юзеров
        self.user_tst = User.objects.create(email="test@test.com", first_name='user_tst', password='user_tst')
        self.user_tst.set_password('user_tst')
        self.user_tst.save()

        self.user_user = User.objects.create(email="user@user.com", first_name='user_user', password='user')
        self.user_user.set_password('user')
        self.user_user.save()

        # Проводим активацию юзера user_tst
        # self.client.force_authenticate(user=self.user_tst)

        # Создаем юзера - модератора
        self.user_moder = User.objects.create(email="mod@mod.com",
                                              first_name='moder',
                                              password='moder',
                                              role='moderator')
        self.user_moder.set_password('moder')
        self.user_moder.save()

        # Создаем объект модели курса (Course)
        self.course_1 = Course.objects.create(
            name="course_name_1"
        )

        # Создаем объект модели урока (Lesson)
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

        # Создаем объект модели подписки (Subscription)
        self.subscription = Subscription.objects.create(
            user=self.user_tst,
            course=self.course_1
        )

    # Тесты
    def test_lesson_list(self):

        """Тест вывода списка уроков"""

        response = self.client.get(reverse('materials:lessons'))
        # print('List lesson\n', response.json())

        # Проверка неавторизованного пользователя
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Авторизация пользователя
        self.client.force_authenticate(user=self.user_tst)

        response = self.client.get(reverse('materials:lessons'))
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

        # Проверка неавторизованного пользователя
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Проверка создания урока модератором
        self.client.force_authenticate(user=self.user_moder)
        response = self.client.post(reverse('materials:lesson_create'), data=data)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

        # Авторизация пользователя
        self.client.force_authenticate(user=self.user_tst)

        response = self.client.post(reverse('materials:lesson_create'), data=data)
        less_id = response.json()["id"]
        # print('Create lesson\n', response.json())
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
        # print('Update lesson\n', response.json())

        # Проверка неавторизованного пользователя
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Авторизация пользователя
        self.client.force_authenticate(user=self.user_tst)

        response = self.client.patch(f'/lesson/update/{self.lesson_1.id}/', data=data)
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
        # print('Retrieve lesson\n', response.json())

        # Проверка неавторизованного пользователя
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Авторизация пользователя
        self.client.force_authenticate(user=self.user_tst)

        response = self.client.get(f'/lesson/{self.lesson_1.id}/')
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
        # print('Delete lesson\n', response.status_code)

        # Проверка неавторизованного пользователя
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Проверка удаления урока модератором
        self.client.force_authenticate(user=self.user_moder)
        response = self.client.delete(f'/lesson/delete/{self.lesson_1.id}/')
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

        # Авторизация пользователя
        self.client.force_authenticate(user=self.user_tst)

        response = self.client.delete(f'/lesson/delete/{self.lesson_1.id}/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_subscription_list(self):

        """Тест вывода списка подписок"""

        # Авторизация пользователя
        self.client.force_authenticate(user=self.user_tst)

        response = self.client.get(reverse('materials:subscription'))
        # print('List subscription', response.json())
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(),
                          [
                              {
                                  "id": self.subscription.id,
                                  "user": self.user_tst.id,
                                  "course": self.course_1.id
                              }
                          ]
                          )

    def test_subscription_create(self):

        """Тест проверки оформления подписки"""

        # Авторизация пользователя
        self.client.force_authenticate(user=self.user_tst)

        data = {
            "course": self.course_1.id
        }

        response = self.client.post(reverse('materials:subscription_create'), data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(),
                          {
                              "message": "Подписка удалена"
                          }
                          )

        response = self.client.post(reverse('materials:subscription_create'), data=data)
        self.assertEquals(response.json(),
                          {
                              "message": "Подписка создана"
                          }
                          )
