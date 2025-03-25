from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Contato, Categoria
from .forms import ContatoForm




def listar_categorias(request):
    """View para listar todas as categorias."""
    categorias = Categoria.objects.all().order_by('nome')
    
    return render(request, 'contatos/listar_categorias.html', {
        'categorias': categorias
    })

def criar_categoria(request):
    """View para criar uma nova categoria."""
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:
            categoria = Categoria(nome=nome)
            categoria.save()
            messages.success(request, 'Categoria criada com sucesso!')
            return redirect('listar_categorias')
        else:
            messages.error(request, 'O nome da categoria não pode estar vazio.')
    
    return render(request, 'contatos/criar_categoria.html')










def index(request):
    """View para a página inicial que lista todos os contatos."""
    # Obter todos os contatos que estão marcados para mostrar
    contatos = Contato.objects.filter(mostrar=True)
    
    # Configuração da paginação
    paginator = Paginator(contatos, 10)  # 10 contatos por página
    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(request, contato_id):
    """View para visualizar os detalhes de um contato específico."""
    # Busca o contato pelo ID ou retorna 404 se não encontrar
    contato = get_object_or_404(Contato, id=contato_id, mostrar=True)
    
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

def busca(request):
    """View para buscar contatos com base em um termo de pesquisa."""
    termo = request.GET.get('termo')
    
    if termo is None or not termo:
        return redirect('index')
    
    # Busca contatos que contenham o termo no nome, sobrenome, telefone ou email
    contatos = Contato.objects.filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo) |
        Q(telefone__icontains=termo) | Q(email__icontains=termo),
        mostrar=True
    )
    
    # Configuração da paginação
    paginator = Paginator(contatos, 10)  # 10 contatos por página
    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })

def criar_contato(request):
    """View para criar um novo contato."""
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.mostrar = True
            contato.save()
            messages.success(request, 'Contato criado com sucesso!')
            return redirect('index')
    else:
        form = ContatoForm()
    
    return render(request, 'contatos/criar_contato.html', {
        'form': form,
        'categorias': Categoria.objects.all()
    })

def editar_contato(request, contato_id):
    """View para editar um contato existente."""
    contato = get_object_or_404(Contato, id=contato_id)
    
    if request.method == 'POST':
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato atualizado com sucesso!')
            return redirect('ver_contato', contato_id=contato.id)
    else:
        form = ContatoForm(instance=contato)
    
    return render(request, 'contatos/editar_contato.html', {
        'form': form,
        'contato': contato
    })

def deletar_contato(request, contato_id):
    """View para deletar um contato."""
    contato = get_object_or_404(Contato, id=contato_id)
    
    if request.method == 'POST':
        contato.delete()
        messages.success(request, 'Contato excluído com sucesso!')
        return redirect('index')
    
    return render(request, 'contatos/deletar_contato.html', {
        'contato': contato
    })