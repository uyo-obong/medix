import jwt
from rest_framework.response import Response
from rest_framework.views import APIView

from medixus.apps.referral.models import UserTable
from medixus.settings import env


class GetAuth(APIView):

    def post(self, request):
        authorization = request.META['HTTP_AUTHORIZATION']
        if not authorization:
            return Response({'status': 400, 'message': 'failed', 'data': 'No Authorization'}, 200)

        token = jwt.decode(authorization, env.str('JWT_TOKEN'), algorithms=["HS256"])

        # Validate customer (TODO: CHNAGE EMAIL TO ID)
        user = UserTable.objects.filter(email=token['email'])

        if not user:
            return Response({'status': 400, 'message': 'failed', 'data': 'Customer not found'}, 200)


        breakpoint()
