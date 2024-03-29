# views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import generics, status
from rest_framework.response import Response
from ..repositories.salaRepository import SalaRepository
from ..serializers.salaSerializer import SalaSerializer

class SalaList(generics.ListCreateAPIView):
    serializer_class = SalaSerializer

    def get_queryset(self):
        repository = SalaRepository()
        return repository.listar_todas()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        repository = SalaRepository()
        sala_id = repository.criar_sala(serializer.validated_data)
        return Response({'id': sala_id}, status=status.HTTP_201_CREATED)

class SalaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SalaSerializer

    def get_object(self):
        repository = SalaRepository()
        return repository.obter_por_id(self.kwargs['pk'])

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        repository = SalaRepository()
        success = repository.atualizar_sala(self.kwargs['pk'], serializer.validated_data)
        if success:
            return Response(serializer.data)
        else:
            return Response({'detail': 'Sala não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        repository = SalaRepository()
        success = repository.excluir_sala(self.kwargs['pk'])
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'Sala não encontrada'}, status=status.HTTP_404_NOT_FOUND)

def listar_salas(request):
    repository = SalaRepository()
    salas = repository.listar_todas()
    return render(request, 'listar_salas.html', {'salas': salas})

def criar_sala(request):
    if request.method == 'POST':
        repository = SalaRepository()
        data = {'nome': request.POST.get('nome'), 'capacidade': request.POST.get('capacidade')}
        sala_id = repository.criar_sala(data)
        return HttpResponseRedirect('/api/salas/')
    else:
        return render(request, 'criar_sala.html')

def atualizar_sala(request, sala_id):
    if request.method == 'POST':
        repository = SalaRepository()
        data = {'nome': request.POST.get('nome'), 'capacidade': request.POST.get('capacidade')}
        success = repository.atualizar_sala(sala_id, data)
        if success:
            return HttpResponseRedirect('/api/salas/')
        else:
            return render(request, 'sala_nao_encontrada.html')
    else:
        repository = SalaRepository()
        sala = repository.obter_por_id(sala_id)
        return render(request, 'atualizar_sala.html', {'sala': sala})

def excluir_sala(request, sala_id):
    repository = SalaRepository()
    success = repository.excluir_sala(sala_id)
    if success:
        return HttpResponseRedirect('/api/salas/')
    else:
        return render(request, 'sala_nao_encontrada.html')
