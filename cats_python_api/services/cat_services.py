from cats_python_api.serializers.cat_serializers import CatSerializer


def save_cat(data: dict) -> dict:
    serializer = CatSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data
