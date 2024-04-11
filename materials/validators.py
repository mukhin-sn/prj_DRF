from rest_framework.exceptions import ValidationError


def validate_link_to_video(value):
    resolved_link = 'youtube.com'
    # if 'youtube.com' not in value:
    #     raise ValidationError('Неразрешенная ссылка')

    # Если адрес содержит разрешенную ссылку (resolved_link),
    # а также перед и/или после разрешенной комбинации символов в ссылке находятся символы "/",
    # то адрес разрешен
    index_start = value.lower().find(resolved_link)
    index_end = value.lower().rfind(resolved_link)
    if index_start != -1 and index_start == index_end:
        if not index_start or value[index_start-1] == "/":
            if len(value) > index_start+len(resolved_link):
                if value[index_start+len(resolved_link)] == '/':
                    return value
            else:
                return value
    raise ValidationError('Неразрешенная ссылка')

