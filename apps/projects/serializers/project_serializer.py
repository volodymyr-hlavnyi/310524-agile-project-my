from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import serializers, status
from rest_framework.views import APIView

from ..models.project import Project


class AllProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['di', 'name', 'created_at']


class CreateProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Project
        fields = ['di', 'name', 'created_at']
        read_only_fields = ['created_at']

        def validate_description(self, value):
            if len(value) < 30:
                raise serializers.ValidationError('Description must be at least 30 characters')
            return value

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['di', 'name', 'created_at', 'count_of_files']


class ProjectDetailAPIView(APIView):
    @staticmethod
    def delete(self, request, pk):
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response(data={'message': f'{project} deleted'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)






