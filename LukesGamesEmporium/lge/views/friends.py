from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from lge.models import FriendRequest, UserProfile, Friends

@login_required
def friendPage(request):
    userMessage = ""

    if request.method == "POST":
        action = request.POST.get('action')
        friendUsername = request.POST.get('username')
        signedInUser = request.user

        if action == "send":
            try:
                friendUser = User.objects.get(username=friendUsername)
                if friendUser == signedInUser:
                    userMessage = "You can't send a friend request to yourself"
                elif Friends.objects.filter(user=signedInUser, friend=friendUser).exists() or Friends.objects.filter(user=friendUser, friend=signedInUser).exists():
                    userMessage = "You are already friends with that user"
                elif FriendRequest.objects.filter(sender=signedInUser, receiver=friendUser).exists():
                    userMessage = "You have already sent a friend request to that user"
                else:
                    friendRequest = FriendRequest.objects.create(sender=signedInUser, receiver=friendUser)
                    friendRequest.save()
                    userMessage = "Friend request sent to " + friendUsername
            except User.DoesNotExist:
                userMessage = "No user with that username"
        elif action == "accept":
            try:
                friendRequest = FriendRequest.objects.get(id=request.POST.get('request_id'))
                newFriends = Friends.objects.create(user=friendRequest.sender, friend=friendRequest.receiver)
                newFriends.save()
                friendRequest.delete()
                userMessage = "Friend request accepted"
            except FriendRequest.DoesNotExist:
                userMessage = "Friend request does not exist"
        elif action == "reject":
            try:
                friendRequest = FriendRequest.objects.get(id=request.POST.get('request_id'))
                friendRequest.delete()
                userMessage = "Friend request rejected"
            except FriendRequest.DoesNotExist:
                userMessage = "Friend request does not exist"

    received_requests = FriendRequest.objects.filter(receiver=request.user)
    sent_requests = FriendRequest.objects.filter(sender=request.user)

    context = {
        "userMessage": userMessage,
        "received_requests": received_requests,
        "sent_requests": sent_requests,
    }
    return render(request, 'friends.html', context)