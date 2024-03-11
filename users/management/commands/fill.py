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
                "password": "111111",
                "is_active": True,
            },
            {
                "pk": 2,
                "email": "petrov@gmail.com",
                "first_name": "Петр",
                "password": "222222",
                "is_active": True,
            },
            {
                "pk": 3,
                "email": "sidorov@gmail.com",
                "first_name": "Сидор",
                "password": "333333",
                "is_active": True,
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
            {"user_id": 1, "paid_course_id": 1, "pay_amount": 150000, "pay_method": "bank transfer"},
            {"user_id": 1, "paid_course_id": 2, "pay_amount": 200000, "pay_method": "bank transfer"},
            {"user_id": 2, "paid_course_id": 3, "pay_amount": 120000, "pay_method": "bank transfer"},
            {"user_id": 2, "paid_lesson_id": 6, "pay_amount": 10000, "pay_method": "bank transfer"},
            {"user_id": 3, "paid_course_id": 1, "pay_amount": 150000, "pay_method": "bank transfer"},
            {"user_id": 3, "paid_course_id": 3, "pay_amount": 120000, "pay_method": "bank transfer"},
            {"user_id": 3, "paid_lesson_id": 5, "pay_amount": 15000, "pay_method": "bank transfer"}
        ]

        User.objects.all().delete()
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Payment.objects.all().delete()

        for_create = []

        for users_item in users_list:
            for_create.append(User(**users_item))
        User.objects.bulk_create(for_create)
        for_create.clear()

        for courses_item in courses_list:
            for_create.append(Course(**courses_item))
        Course.objects.bulk_create(for_create)
        for_create.clear()

        for lessons_item in lessons_list:
            for_create.append(Lesson(**lessons_item))
        Lesson.objects.bulk_create(for_create)
        for_create.clear()

        for payments_item in payments_list:
            for_create.append(Payment(**payments_item))
        Payment.objects.bulk_create(for_create)
        for_create.clear()
