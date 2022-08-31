from django.contrib.auth.models import User, Group
from django.contrib.auth.models import User
from rest_framework import serializers
from p1.models import Questions, Options, Test, Answers


class TestsSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField('get_question_count')
    class Meta:
        model = Test
        fields = ['id','title','description','question_count','estimated_time', 'created_at', 'updated_at']

    def get_question_count(self, test):
        return Questions.objects.filter(Test = test.id).count()


class optionsubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['Option_Text']

class getTestSerializer(serializers.ModelSerializer):
    Test = serializers.SerializerMethodField('get_Test')
    option = optionsubSerializer(many=True)
    class Meta:
        model = Questions
        fields = ['Test', 'Question_Text', 'option', 'created_at', 'updated_at']


    def get_Test(self, question):
        return question.Test.title


class QuestionsSerializer(serializers.ModelSerializer):
    TestName = serializers.SerializerMethodField('get_test')
    class Meta:
        model = Questions
        fields = ['Test', 'TestName','Question_Text', 'created_at', 'updated_at']

    def get_test(self, question):
        return question.Test.title

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = "__all__"



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AnswersSerializer(serializers.ModelSerializer):
    OptionName = serializers.SerializerMethodField('get_Option')
    user_name = serializers.SerializerMethodField('get_user')
    class Meta:
        model = Answers
        fields = ['number','Option','OptionName','user','user_name', 'created_at', 'updated_at']

    def get_Option(self, answer):
        return answer.Option.Option_Text

    def get_user(self, answer):
        return answer.user.username