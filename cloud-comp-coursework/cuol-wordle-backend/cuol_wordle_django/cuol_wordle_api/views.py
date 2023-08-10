from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes, throttle_classes,permission_classes
from .serializers import WordSerializer, UserStatsSerializer, GuessDistributionSerializer
from .models import Word, UserStats, GuessDistribution

from rest_framework.permissions import IsAuthenticated

# Generic for testing


class WordView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    model = Word
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class UserStatsView(generics.ListAPIView):
    queryset = UserStats.objects.all()
    serializer_class = UserStatsSerializer


class GuessDistributionView(generics.ListAPIView):
    queryset = GuessDistribution.objects.all()
    serializer_class = GuessDistributionSerializer


def get_value(request):
    return request.data['value']


@api_view(['POST'])
@parser_classes([JSONParser])
@permission_classes([IsAuthenticated])
# @throttle_classes([OncePerDayUserThrottle])
def check_chosen(request):
    print(request)
    word = request.data['chosen_word']
    # LENGTH CHECKS if user submitted is equal to the chosen one
    # Update the stats
    is_chosen = False
    if word == 'HOUSE':
        is_chosen = True
    #id_picked = get_value(request)
    #champion:Champion = Champion.objects.get(id=id_picked)
    return JsonResponse({"is_chosen": is_chosen})


def stats(request):
    pass
