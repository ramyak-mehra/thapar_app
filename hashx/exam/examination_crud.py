import graphene
from .models import Examination
from graphql_relay.node.node import from_global_id
from .schema import ExaminationNode
from graphene_django.types import DjangoObjectType
from hashx.decorators import every_authenticated , same_user , compare_users
class CreateExamination(graphene.relay.ClientIDMutation):
    examination = graphene.Field(ExaminationNode)
    class Input:
        type = graphene.String()
        
    
    @classmethod
    @every_authenticated
    def mutate_and_get_payload(cls,root, info, **input):
        type = input.get('type')
        examination = Examination(type=type)
        examination.save()
        return  CreateExamination(examination=examination)
class UpdateExamination(graphene.relay.ClientIDMutation):
    examination = graphene.Field(ExaminationNode)
    class Input:
        id = graphene.String()
        type = graphene.String()
        
    @classmethod
    @every_authenticated
    @compare_users(same_user , Examination)
    def mutate_and_get_payload(cls,root, info, **input):
        id = input.get('id')
        id = from_global_id(id)
        id = id[1]
        examination = Examination.objects.get(pk=id)
        type = input.get('type')
        if type:
            examination.type = type
        examination.save()
        return UpdateExamination(examination=examination)