from rest_framework.exceptions import ValidationError


def validate_link_to_video(value):
    if 'youtube.com' not in value:
        raise ValidationError('Неразрешенная ссылка')
    return value
