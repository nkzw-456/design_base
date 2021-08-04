# ListViewとDetailViewを取り込み
from django.views.generic import ListView, DetailView

from .models import Post
from django.db.models import Q
# ListViewは一覧を簡単に作るためのView
class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = Post
    def get_queryset(self):
        q_word = self.request.GET.get('query')
 
        if q_word:
            object_list = Post.objects.filter(
                Q(first_name=q_word) | Q(last_name=q_word))
        else:
            object_list = Post.objects.all()
        return object_list

# DetailViewは詳細を簡単に作るためのView
class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    model = Post

from django.views.generic.edit import CreateView, UpdateView
from .forms import TextForm, updateform

# CreateViewは新規作成画面を簡単に作るためのView
class Create(CreateView):
    model = Post
    form_class = TextForm

class Update(UpdateView):
    template_name = 'design_app/update.html'
    model = Post
    form_class = updateform

from django.views.generic import DeleteView
class Delete(DeleteView):
    model = Post
    success_url = '/'
