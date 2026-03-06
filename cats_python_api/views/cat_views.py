from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cats_python_api.models.core_models import Cat
from cats_python_api.services.cat_services import save_cat


@api_view(['GET'])
def cats_list(request):
    cats = Cat.objects.all().values('id', 'cat_id', 'url', 'width', 'height', 'breeds', 'api_used', 'created_at', 'updated_at')
    return Response(list(cats))


def _is_duplicate_key_error(exc: BaseException) -> bool:
    msg = str(exc).lower()
    return "unique" in msg or "duplicate key" in msg or "cats_cat_id" in msg


@api_view(['POST'])
def cat_save(request):
    try:
        data = {**request.data, "api_used": "python"}
        cat = save_cat(data)
        return Response(cat, status=status.HTTP_201_CREATED)
    except IntegrityError as e:
        if _is_duplicate_key_error(e):
            return Response(
                {"detail": "Ya existe un gato con este ID en la base de datos."},
                status=status.HTTP_409_CONFLICT,
            )
        raise
    except Exception as e:
        if _is_duplicate_key_error(e):
            return Response(
                {"detail": "Ya existe un gato con este ID en la base de datos."},
                status=status.HTTP_409_CONFLICT,
            )
        raise