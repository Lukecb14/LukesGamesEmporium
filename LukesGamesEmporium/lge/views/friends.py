from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lge.models import Score, Game
from django.contrib.auth.models import User
from lge.models import FriendRequest

@login_required
def friendPage(request):
    
    userMessage = ""

    if request.method == "POST":
        signedInUser = request.user
        friendUsername = request.POST.get('username')

        # TODO: prevent code injections (idk if that's necessary in Django, but can't hurt to check)
        try:
            friendUser = User.objects.get(username=friendUsername)
            if friendUser == signedInUser:
                userMessage = "You can't send a friend request to yourself"
            elif FriendRequest.objects.filter(sender=signedInUser, receiver=friendUser).exists():
                userMessage = "You have already sent a friend request to that user"
            else:
                friendRequest = FriendRequest.objects.create(sender=signedInUser, receiver=friendUser)
                friendRequest.save()
                userMessage = "Friend request sent to " + friendUsername
        except:
            userMessage = "No user with that username"

    context = {
        "userMessage": userMessage    
    }
    return render(request, 'friends.html', context)