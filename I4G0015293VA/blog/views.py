from .models import Post

def PostListView():
    model = Post

def PostCreateView():
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")


def PostDetailView():
    model = Post


def PostUpdateView():
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

def PostDeleteView():
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")



# Create your views here.
