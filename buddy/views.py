from rest_framework import status, generics
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# @csrf_exempt
@api_view(['GET', 'POST'])
def book_list(request):
    # Retrieve or update the book list.
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getBook(request, pk):
    # Retrieve, update or delete an book instance.
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def author_list(request):
    # Retrieve or update the author list.
    if request.method == 'GET':
        author = Author.objects.all()
        serializer = AuthorSerializer(author, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getAuthor(request, pk):
    # Retrieve, update or delete an Author.
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(author, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def review_list(request):
    # Retrieve or update the review list.
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getReview(request, pk):
    # Retrieve, update or delete a review instance.
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def book_buddy_list(request):
    # Retrieve or update the review list.
    if request.method == 'GET':
        book_buddy = BookBuddy.objects.all()
        serializer = BookBuddySerializer(book_buddy, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = BookBuddySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getBookBuddy(request, pk):
    # Retrieve, update or delete a review instance.
    try:
        book_buddy = BookBuddy.objects.get(pk=pk)
    except BookBuddy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookBuddySerializer(book_buddy, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookBuddySerializer(book_buddy, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book_buddy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterView(generics.CreateAPIView):
    # Register a new user - requester need not be authorized
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getUser(request):
    # Request the information about the user making the request
    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
