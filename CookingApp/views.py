from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from CookingApp.models import Recipe, Comment
from CookingApp.serializer import RecipeSerializer, CommentSerializer


class RecipeCreateApi(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeGetApi(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        creator_id = self.request.query_params.get('creator_id')
        search = self.request.query_params.get('search')
        if creator_id is not None:
            queryset = queryset.filter(creator_id=creator_id)
        if search is not None:
            queryset = queryset.filter(name__icontains=search)
        return queryset


@api_view(['GET'])
def api_detail_recipe_view(request, pk):
    try:
        recipe = Recipe.objects.get(id=pk)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_update_recipe_view(request, pk):
    user_id = str(request.user.pk)
    try:
        recipe = Recipe.objects.get(id=pk)
        creator_id = str(recipe.creator_id.id)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if creator_id != user_id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        request.data['creator_id'] = user_id
        serializer = RecipeSerializer(recipe, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_delete_recipe_view(request, pk):
    user_id = str(request.user.pk)

    try:
        recipe = Recipe.objects.get(id=pk)
        creator_id = str(recipe.creator_id.id)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        if creator_id != user_id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        operation = recipe.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_create_recipe_view(request):
    request.data['creator_id'] = request.user.pk
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_create_comment_view(request, recipe_id):
    comment = {}
    if isinstance(request.data, str):
        comment['content'] = request.data
    else:
        comment['content'] = request.data['content']
    comment['author_id'] = request.user.username
    comment['recipe'] = recipe_id
    serializer = CommentSerializer(data=comment)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@api_view(['GET'])
def api_get_comment_view(request, recipe_id):
    comments = Comment.objects.filter(recipe=recipe_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(status=status.HTTP_200_OK, data=serializer.data)