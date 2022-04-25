from .models import Poll, Choice, Vote
from rest_framework import serializers, viewsets, permissions
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

# Serializers define the API representation.
class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'owner', 'text', 'pub_date']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'poll', 'choice_text']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['user', 'poll', 'choice']


# ViewSets define the view behavior.
class PollViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
      polls = Poll.objects.filter(active=False)
      serializer = PollSerializer(polls, many=True)
      return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        return JsonResponse("Facility not available", status=400, safe=False)
   
    def retrieve(self, request, pk=None):
        try:
            poll_model = Poll.objects.get(id=pk)
            serializer = PollSerializer(poll_model)
            return JsonResponse(serializer.data)
        except Poll.DoesNotExist:
            return HttpResponse(status=404)

    def update(self, request, pk=None):
        return JsonResponse("Facility not available", status=400, safe=False)

    def destroy(self, request, pk=None):
        return JsonResponse("Facility not available", status=400, safe=False)

class ChoiceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
      choices = Choice.objects.select_related("poll").all()
      serializer = ChoiceSerializer(choices, many=True)
      return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        return JsonResponse("Facility not available", status=400, safe=False)
   
    def retrieve(self, request, pk=None):
        try:
            choice_model = Choice.objects.get(id=pk)
            serializer = ChoiceSerializer(choice_model)
            return JsonResponse(serializer.data)
        except Choice.DoesNotExist:
            return HttpResponse(status=404)

    def update(self, request, pk=None):
        return JsonResponse("Facility not available", status=400, safe=False)

    def destroy(self, request, pk=None):
        return JsonResponse("Facility not available", status=400, safe=False)

class VoteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
      return JsonResponse("Facility not available", status=400, safe=False)

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
   
    def retrieve(self, request, pk=None):
        return JsonResponse("Facility not available", status=400, safe=False)

    def update(self, request, pk=None):
        vote_model = Vote.objects.get(id=pk)
        data = JSONParser().parse(request)
        serializer = VoteSerializer(vote_model, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        return JsonResponse("Facility not available", status=400, safe=False)