from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Board
from .serializers import BoardSerializer

@api_view(['POST'])
def create_board(request):
    serializer=BoardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_boards(request):
    boards=Board.objects.all()
    serializer=BoardSerializer(boards,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_board(request, pk):
    try:
        board=Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        return Response({'error':'Board not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer=BoardSerializer(board)
    return Response(serializer.data)

@api_view(['PUT','PATCH'])
def update_board(request,pk):
    try:
        board=Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        return Response({'error':'Board not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer=BoardSerializer(board, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_board(request, pk):
    try:
        board=Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        return Response({'error':'Board not found'}, status=status.HTTP_404_NOT_FOUND)
    
    board.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
        