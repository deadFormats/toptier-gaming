from django.shortcuts import render, get_object_or_404
from .models import TeamPost

# Create your views here.
def team_post_list(request):
    team_posts = TeamPost.published.all()
    return render(
        request,
        'teamlink/team_post/list.html',
        {'team_posts': team_posts}
    )


def team_post_detail(request, id):
    team_post = get_object_or_404(
        TeamPost,
        id=id,
        status=TeamPost.Status.PUBLISHED
    )
    return render(
        request,
        'teamlink/team_post/detail.html',
        {'team_post': team_post}
    )
