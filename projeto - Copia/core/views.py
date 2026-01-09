from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Pessoa
from .serializers import PessoaSerializer

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})

def salvar(request):
    if request.method != 'POST':
        return redirect('home')

    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    curso = request.POST.get('curso')
    periodo = request.POST.get('periodo')
    opiniao = request.POST.get('opiniao')
    foto = request.FILES.get('foto')

    if not nome or not idade:
        return redirect('home')

    Pessoa.objects.create(
        nome=nome,
        idade=int(idade),
        curso=curso,
        periodo=periodo,
        opiniao=opiniao,
        foto=foto
    )

    return redirect('home')
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == 'POST':
        pessoa.nome = request.POST.get('nome')
        pessoa.idade = request.POST.get('idade')
        pessoa.curso = request.POST.get('curso')
        pessoa.periodo = request.POST.get('periodo')
        pessoa.opiniao = request.POST.get('opiniao')

        if 'foto' in request.FILES:
            pessoa.foto = request.FILES['foto']

        pessoa.save()
        return redirect('home')

    return render(request, 'editar.html', {'pessoa': pessoa})
def deletar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.delete()
    return redirect('home')
def api_hello(request):
    return JsonResponse({
        "mensagem": "Olá! Django conectado com React 🚀"
    })
@api_view(['GET'])
def api_test(request):
    return Response({
        "mensagem": "API Django conectada com sucesso 🚀"
    })
@api_view(['GET', 'POST'])
def pessoa_list_create(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data)

    serializer = PessoaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def pessoa_detail(request, id):
    print("DATA:", request.data)
    print("FILES:", request.FILES)

    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == 'GET':
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PessoaSerializer(pessoa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    pessoa.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
