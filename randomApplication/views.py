# from http.client import HTTPResponse
from django.shortcuts import HttpResponse
from.models import FriendRequest,User, blockList
from rest_framework.decorators import api_view
from rest_framework import viewsets
from randomApplication.serializers import UserSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
# from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated  

# Create your views here.

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)


    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            if serializer.data.get("new_password") == serializer.data.get("confirm_password"):
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)
            return Response({"confirm_password": ["Re enter your password"]}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



@api_view(['POST'])
def send_friend_request(request, UserID):
    from_user =request.user
    to_user = User.objects.get(id = UserID) 
    # print(from_user)
    blockusers=blockList.objects.filter(to_user=from_user,from_user=to_user)
    print("-----",blockusers)
    # if from_user == to_user.id:
    # print(to_user)
    Friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)

    if created:
        return HttpResponse('Friend Request Sent')



@api_view(['POST'])
def accept_friend_request(request, requestID):
    Friend_request = FriendRequest.objects.get(id = requestID)
    print("from_user",Friend_request.from_user)
    print("to_user",Friend_request.to_user)
    if Friend_request.to_user == request.user:
        Friend_request.to_user.friends.add(Friend_request.from_user)
        Friend_request.from_user.friends.add(Friend_request.to_user)
        Friend_request.delete()
        return HttpResponse('Friend Request Accepted / You Are Now Friends')
    else:
        return HttpResponse('Friend Request Rejected')



@api_view(['POST'])
def ignore_friend_request(request, requestID):
    Friend_request = FriendRequest.objects.get(id = requestID)
    print("from_user",Friend_request.from_user)
    print("to_user",Friend_request.to_user)
    if Friend_request.to_user == request.user:
        Friend_request.delete()
        return HttpResponse('Friend Request Deleted')
    else:
        return HttpResponse('Error')



@api_view(['POST'])
def revert_friend_request(request, requestID):
    Friend_request = FriendRequest.objects.get(id = requestID)
    print("from_user",Friend_request.from_user)
    print("to_user",Friend_request.to_user)
    if Friend_request.from_user == request.user:
        Friend_request.delete()
        return HttpResponse('Your Request Is Cancelled')
    else:
        return HttpResponse('Cancel Request Error')


@api_view(['POST'])
def block_friend_request(request, userID):
    user=request.user
    to_user = User.objects.get(id = userID)
    Friend_request, created = blockList.objects.get_or_create(from_user=user, to_user=to_user)
    # Friend_request = blockList.objects.get(id = userID)
    Friend_request.to_user.blockList.add(Friend_request.from_user)
    Friend_request.from_user.blockList.add(Friend_request.to_user)
    print("from_user",Friend_request.from_user)
    print("to_user",Friend_request.to_user)
    if created:
        return HttpResponse('User has been blocked')
    return HttpResponse('User Already Blocked by you')


