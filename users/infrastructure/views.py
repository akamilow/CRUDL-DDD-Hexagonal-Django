# Controladores/API. Adaptan HTTP a los casos de uso, desacoplando el framework.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
from users.infrastructure.repositories import DjangoUserRepository
from users.application.use_cases import (
    RegisterUserUseCase, GetUserProfileUseCase, UpdateUserUseCase,
    DeleteUserUseCase, ListUsersUseCase, LoginUseCase
)
from users.domain.exceptions import UserAlreadyExists, UserNotFound, InvalidCredentials

repo = DjangoUserRepository()

@method_decorator(csrf_exempt, name='dispatch')
class RegisterUserView(View):
    def post(self, request):
        data = json.loads(request.body)
        use_case = RegisterUserUseCase(repo)
        try:
            user = use_case.execute(
                data["nombre"], data["apellido"], data["email"],
                data["telefono"], data["password"]
            )
            return JsonResponse({"id": user.id, "email": user.email})
        except UserAlreadyExists:
            return JsonResponse({"error": "Email ya registrado"}, status=400)

class GetUserProfileView(View):
    def get(self, request, user_id):
        use_case = GetUserProfileUseCase(repo)
        try:
            user = use_case.execute(user_id)
            return JsonResponse({
                "id": user.id, "nombre": user.nombre, "apellido": user.apellido,
                "email": user.email, "telefono": user.telefono
            })
        except UserNotFound:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateUserView(View):
    def put(self, request, user_id):
        data = json.loads(request.body)
        use_case = UpdateUserUseCase(repo)
        try:
            user = use_case.execute(
                user_id, data["nombre"], data["apellido"], data["telefono"]
            )
            return JsonResponse({"id": user.id, "email": user.email})
        except UserNotFound:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class DeleteUserView(View):
    def delete(self, request, user_id):
        use_case = DeleteUserUseCase(repo)
        try:
            use_case.execute(user_id)
            return JsonResponse({"message": "Usuario eliminado"})
        except UserNotFound:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)

class ListUsersView(View):
    def get(self, request):
        use_case = ListUsersUseCase(repo)
        users = use_case.execute()
        return JsonResponse([
            {
                "id": u.id, "nombre": u.nombre, "apellido": u.apellido,
                "email": u.email, "telefono": u.telefono
            } for u in users
        ], safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        use_case = LoginUseCase(repo)
        try:
            result = use_case.execute(data["email"], data["password"])
            return JsonResponse(result)
        except InvalidCredentials:
            return JsonResponse({"error": "Credenciales inválidas"}, status=401)
