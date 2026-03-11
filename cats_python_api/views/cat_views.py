from django.db import IntegrityError
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cats_python_api.models.core_models import Cat
from cats_python_api.serializers.cat_serializers import CatSerializer
from cats_python_api.services.cat_services import save_cat


@api_view(['GET'])
def cats_list(request):
    try:
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(
            {"detail": "Error al obtener la lista de gatos"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(['GET'])
def cat_get_by_id(request, id):
    try:
        cat = Cat.objects.get(id=id)
        serializer = CatSerializer(cat)
        return Response(serializer.data)
    except Cat.DoesNotExist:
        return Response(
            {"detail": "Gato no encontrado"},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception:
        return Response(
            {"detail": "Error al obtener el gato"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(['GET'])
def cat_get_by_cat_id(request, cat_id):
    try:
        cat = Cat.objects.get(cat_id=cat_id)
        serializer = CatSerializer(cat)
        return Response(serializer.data)
    except Cat.DoesNotExist:
        return Response(
            {"detail": "Gato no encontrado"},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception:
        return Response(
            {"detail": "Error al obtener el gato"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(['POST'])
def cat_save(request):
    try:
        data = {**request.data, "api_used": "python"}
        cat = save_cat(data)
        return Response(cat, status=status.HTTP_201_CREATED)
    except IntegrityError as e:
        if _is_duplicate_key_error(e):
            return Response(
                {"detail": "Ya existe un gato con este ID en la base de datos"},
                status=status.HTTP_409_CONFLICT,
            )
        raise
    except Exception:
        return Response(
            {"detail": "Error al guardar el gato"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(['PUT'])
def cat_update(request, id):
    try:
        cat = Cat.objects.get(id=id)
        data = {**request.data, "api_used": "python"}
        serializer = CatSerializer(cat, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    except Cat.DoesNotExist:
        return Response(
            {"detail": "Gato no encontrado"},
            status=status.HTTP_404_NOT_FOUND,
        )
    except ValidationError as e:
        return Response(
            {"detail": e.detail},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception:
        return Response(
            {"detail": "Error al actualizar el gato"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(['DELETE'])
def cat_delete(request, id):
    try:
        cat = Cat.objects.get(id=id)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Cat.DoesNotExist:
        return Response(
            {"detail": "Gato no encontrado"},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception:
        return Response(
            {"detail": "Error al eliminar el gato"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def _is_duplicate_key_error(exc: BaseException) -> bool:
    msg = str(exc).lower()
    return "unique" in msg or "duplicate key" in msg or "cats_cat_id" in msg
