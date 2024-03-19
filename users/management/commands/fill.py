from django.core.management import BaseCommand

from users.models import User, Payment
from materials.models import Course, Lesson


class Command(BaseCommand):

    def handle(self, *args, **options):
        users_list = [
            {
                "pk": 1,
                "email": "ivanov@gmail.com",
                "first_name": "Иван",
                "last_name": "Иванов",
                "password": "111111",
                "is_active": True,
                "is_staff": True,
                "is_superuser": True,
                "city": "Ынахсыт",
            },
            {
                "pk": 2,
                "email": "petrov@gmail.com",
                "first_name": "Петр",
                "last_name": "Петров",
                "password": "222222",
                "is_active": True,
                "is_staff": True,
                "is_superuser": False,
                "city": "Ытык-Кюёль",
            },
            {
                "pk": 3,
                "email": "sidorov@gmail.com",
                "first_name": "Сидор",
                "last_name": "Сидоров",
                "password": "333333",
                "is_active": True,
                "is_staff": False,
                "is_superuser": False,
                "city": "Ыллымах",
            }

        ]

        courses_list = [
            {"pk": 1, "name": "Pytho develop", },
            {"pk": 2, "name": "Java develop", },
            {"pk": 3, "name": "JavaScript", }
        ]

        lessons_list = [
            {"pk": 1, "name": "Django", "course_id": 1},
            {"pk": 2, "name": "DRF", "course_id": 1},
            {"pk": 3, "name": "React", "course_id": 3},
            {"pk": 4, "name": "Angular", "course_id": 3},
            {"pk": 5, "name": "Java for beginners", "course_id": 2},
            {"pk": 6, "name": "Git", "course_id": 1}
        ]

        payments_list = [
            {
                "user_id": 1,
                "paid_course_id": 1,
                "pay_amount": 150000,
                "pay_method": "bank transfer",
                "date_of_pay": "2022-10-25"
            },
            {
                "user_id": 1,
                "paid_course_id": 2,
                "pay_amount": 200000,
                "pay_method": "cash",
                "date_of_pay": "2022-12-5"
            },
            {
                "user_id": 2,
                "paid_course_id": 3,
                "pay_amount": 120000,
                "pay_method": "bank transfer",
                "date_of_pay": "2021-7-21"
            },
            {
                "user_id": 2,
                "paid_lesson_id": 6,
                "pay_amount": 10000,
                "pay_method": "bank transfer",
                "date_of_pay": "2022-5-15"
            },
            {
                "user_id": 3,
                "paid_course_id": 1,
                "pay_amount": 150000,
                "pay_method": "cash",
                "date_of_pay": "2023-6-6"
            },
            {
                "user_id": 3,
                "paid_course_id": 3,
                "pay_amount": 120000,
                "pay_method": "bank transfer",
                "date_of_pay": "2023-9-13"
            },
            {
                "user_id": 3,
                "paid_lesson_id": 5,
                "pay_amount": 15000,
                "pay_method": "cash",
                "date_of_pay": "2022-12-20"
            }
        ]

        def load_data_to_db(cls, list_data):
            data_load = []
            cls.objects.all().delete()
            for item_ in list_data:
                if "password" in item_:
                    user = cls.objects.create(
                        email=item_["email"],
                        pk=item_["pk"],
                        first_name=item_["first_name"],
                        last_name=item_["last_name"],
                        city=item_["city"],
                        is_superuser=item_["is_superuser"],
                        is_staff=item_["is_staff"],
                        is_active=item_["is_active"]
                    )
                    user.set_password(item_["password"])
                    user.save()
                else:
                    data_load.append(cls(**item_))
            if data_load:
                cls.objects.bulk_create(data_load)

        load_data_to_db(User, users_list)
        load_data_to_db(Course, courses_list)
        load_data_to_db(Lesson, lessons_list)
        load_data_to_db(Payment, payments_list)

        # User.objects.all().delete()
        # Course.objects.all().delete()
        # Lesson.objects.all().delete()
        # Payment.objects.all().delete()

        # for_create = []

        # for users_item in users_list:
        #     for_create.append(User(**users_item))
        # User.objects.bulk_create(for_create)
        # for_create.clear()

        # for courses_item in courses_list:
        #     for_create.append(Course(**courses_item))
        # Course.objects.bulk_create(for_create)
        # for_create.clear()
        #
        # for lessons_item in lessons_list:
        #     for_create.append(Lesson(**lessons_item))
        # Lesson.objects.bulk_create(for_create)
        # for_create.clear()
        #
        # for payments_item in payments_list:
        #     for_create.append(Payment(**payments_item))
        # Payment.objects.bulk_create(for_create)
        # for_create.clear()
