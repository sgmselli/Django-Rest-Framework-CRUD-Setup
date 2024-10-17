from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_item(request):
    data = request.data
    item = Item.objects.create(
        name=data['name']
    )
    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_item(request, pk):
    data = request.data

    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response('id doesnt exist')
    
    serializer = ItemSerializer(item, data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response('id doesnt exist')
    item.delete()
    return Response(status=HTTP_204_NO_CONTENT)
    