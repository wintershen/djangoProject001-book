from django.shortcuts import render, HttpResponse, redirect, reverse
from app01.models import User, Press, Book, Author
from app01 import models


def login1(request):
    return HttpResponse("OK")


def login(request):
    return render(request, "login.html")


def index(request):
    return render(request, "index1.html")


def main(request):
    return render(request, "main.html")


def try_login(request):
    error_msg = ""
    # print(request.POST)
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['pwd']
        print(username, pwd)
        ret = User.objects.filter(username=username, pwd=pwd)
        # if username == "winter" and pwd == "winter123456":
        if ret:
            # 从数据库查询是否有对应的用户.
            # select * from user where email ='winter' and pwd = '123';

            return redirect("/index/")
        else:
            error_msg = "用户名或密码错误"
        return render(request, 'main.html', {'error_msg': error_msg})


# -----day 60 ↓ ------------------

def press_list(request):
    # 1. 去数据库查询所有出版社
    ret = Press.objects.all()
    # print(ret)

    # 2. HTML上去展示
    return render(request, "list/press_list.html", {'ret': ret})


from django.views import View


class AddPress(View):
    def get(self, request):
        return render(request, 'add_press.html')

    def post(self, request):
        # 表示用户填写完了,在发数据
        # 1.取到用户填写的数据
        press_name = request.POST.get('name')
        # 2.把用户填写的数据写到数据库里
        Press.objects.create(name=press_name)
        # 3.返佣列表页面给用户
        return redirect('/press_list/')


def add_press(request):
    if request.method == 'POST':
        # 表示用户填写完了,在发数据
        # 1.取到用户填写的数据
        press_name = request.POST.get('name')
        # 2.把用户填写的数据写到数据库里
        Press.objects.create(name=press_name)
        # 3.返佣列表页面给用户
        return redirect('/press_list/')

    # 1.返回一个添加页面,让用户填写
    return render(request, 'add_press.html')


def delete_press(request):
    # 1.获取要删除的出版社
    delete_id = request.GET.get('id')
    # 2.根据id去数据库删除对应的数据行
    Press.objects.filter(id=delete_id).delete()
    # 3.返回列表查看
    return redirect('/press_list/')


def edit_press(request):
    if request.method == "POST":
        # 收到要修改的请求.
        # 1.取出用户编辑后的name.
        edit_id2 = request.GET.get('id')  # 测试 GET无法获取post提供的id信息.
        print('-' * 120)
        print('edit_id2=', edit_id2)
        print('-' * 120)
        new_name = request.POST.get('name')
        edit_id = request.POST.get('id')
        # 2.去数据库修改对应的数据
        # 2.1.先去找对应的数据
        edit_press = Press.objects.get(id=edit_id)
        # 2.2更新数据
        edit_press.name = new_name
        # 2.3 保存数据同步到数据库
        edit_press.save()
        # 3.返回
        return redirect('/press_list/')

    # 1.获取要编辑的出版社
    edit_id = request.GET.get('id')
    # 2.根据id去获取出版社的信息
    ret = Press.objects.filter(id=edit_id)[0]  # 找出的结果是列表里面的[对象]
    # ret= Press.objects.get(id=edit_id)   #有且只有一个的时候可以找到.
    # 3.在页面上展示对应的消息
    return render(request, 'edit_press.html', {'press_obj': ret})


# def edit_press_old(request):
#     # 1. 从URL中获取要编辑的出版社的id
#     edit_id = request.GET.get('id')
#     print('-' * 60, '进入程序', '-' * 6)
#     print('edit_id=', edit_id)
#     print('-' * 120)
#
#     if request.method == 'POST':
#         # 用户修改完出版社数据给我发过来了
#         # 1.取出用户编辑之后的数据
#         new_name = request.POST.get('name')
#         # 2. 去数据库修改对应的数据
#         # 2.1 先找对应的数据：出版社对象
#         print('-' * 60, '进入POST程序', '-' * 6)
#         print('edit_id=', edit_id)
#         print('-' * 120)
#         edit_press_obj = Press.objects.get(id=edit_id)
#         # 2.2 修改出版社的名称
#         edit_press_obj.name = new_name
#         # 2.3 将修改同步到数据库
#         edit_press_obj.save()
#         # 3. 让用户再去访问出版社列表页
#         return redirect('/press_list/')
#
#     # 2. 获取该出版社的信息
#     # ret = Press.objects.filter(id=edit_id)  # -->[Press obj, ]
#     # print(ret)
#     # print('#' * 120)
#     ret = Press.objects.get(id=edit_id)  # --> Press Obj, get()有且只能找到一个对象，否则就报错
#     # print(ret)
#     # 3. 在页面上展示出来
#     return render(request, 'edit_press.html', {'press_obj': ret})

def edit_press2(request):
    return render(request, 'edit_press2_test.html')


# -----day 61 ↓ ------------------

def book_list(request):
    # 1.查询all book
    list_book = Book.objects.all()
    # 2.展示all book
    # 3.返回html
    return render(request, 'list/book_list.html', {'list_book': list_book})


def add_book(request):
    if request.method == "POST":
        book_title = request.POST.get('book_title')
        press_id = request.POST.get('press_id')
        # 取到用户数据
        # 创建新的记录
        Book.objects.create(title=book_title, press_id=press_id)
        # 基于外键对象的创建
        # press_obj = Press.objects.get(id=press_id)
        # Book.objects.create(title=book_title, press=press_obj)
        # 返回list页面
        return redirect('/book_list/')
    # 1. 返回页面,让用户输入信息
    # 2. 需要展示对应的出版社给客户展示,让客户选择,注意单选.
    press_list = Press.objects.all()
    return render(request, 'add_book.html', {'press_list': press_list})


def delete_book(request):
    # 1.从url中取得要删除的书籍id值
    delete_book_id = request.GET.get('id')
    print(delete_book_id)
    # 2.根据id值去数据库找到对应的数据,并删除掉从
    Book.objects.filter(id=delete_book_id).delete()
    # 3.返回booklist
    return render(request, 'delete_success.html')
    # return redirect('/book_list/')


def edit_book(request):
    if request.method == 'POST':
        # 获取对象,修改信息,保存到数据库,跳转list

        new_title = request.POST.get('book_title')
        new_press_id = request.POST.get('press_id')
        edit_book_id = request.POST.get('id')
        edit_book_obj = Book.objects.get(id=edit_book_id)
        edit_book_obj.title = new_title
        edit_book_obj.press_id = new_press_id
        edit_book_obj.save()
        return redirect('/book_list/')
    # 1.从URL取要编辑书籍id
    edit_book_id = request.GET.get("id")
    # 2.查找对象,获取信息
    edit_book_obj = Book.objects.get(id=edit_book_id)
    press_list = Press.objects.all()
    # 3.在修改页面显示对应的信息,等待被编辑
    return render(request,
                  'edit_book.html',
                  {'book_obj': edit_book_obj, 'press_list': press_list}
                  )


def author_list(request):
    # 1.db查询
    author_list = Author.objects.all()
    # for author in author_list:
    #     print(author)
    #     print(author.books)  # 是一个ORM提供的桥梁(工具),帮我找对应关系.
    #     print(author.books.all())

    # 2.展示
    # return HttpResponse("OK")
    return render(request, 'list/author_list.html', {'author_list': author_list})


def add_author(request):
    if request.method == "POST":
        # 2.1 获取网页信息.
        # 2.1.1 多选,需要获取列表,get只能获得单个值,获取到个值需要getlist
        # 2.2 写入数据库
        # 2.2.1 写入作者表
        # 2.2.2 写入关系表,通过新建立的作者的对象,来添加.
        # 2.2.2.1 obj.books.add(1,2,3)  参数是一个个的值.
        # 2.2.2.1 obj.books.add(*book_ids)  参数是一个个的值.
        # 2.2.2.2 obj.books.set(book_ids)  参数是一个list
        # 2.3 跳转到列表页面
        add_author_name = request.POST.get('author_name')
        book_ids = request.POST.getlist('book_ids')
        new_author_obj = Author.objects.create(name=add_author_name)
        new_author_obj.books.add(*book_ids)
        return redirect('/author_list/')
    # 1.返回页面,让用户填写信息.
    # 2.获取所有书籍信息
    book_list = Book.objects.all()
    return render(request, 'add_author.html', {'book_list': book_list})


def delete_author(request):
    # 1.取值
    delete_author_id = request.GET.get('id')
    # 2.数据库找,并删除
    Author.objects.filter(id=delete_author_id).delete()
    # 待测试,删除了id后,对应的关系,在关系表格里面是如何处理的?
    # 都会同步一起删除.
    # 3.返回页面
    return redirect('/author_list/')


def edit_author(request):
    # 1.获取ID信息,获取数据库信息,显示到对应的页面上.
    edit_author_id = request.GET.get('id')
    edit_author_obj = Author.objects.get(id=edit_author_id)
    if request.method == "POST":
        # 1.拿到编辑后的数据集, 拿到数据
        # 2.更新数据库,并记录
        new_author_name = request.POST.get('author_name')
        new_book_ids = request.POST.getlist('book_ids')
        edit_author_obj.name = new_author_name
        edit_author_obj.save()
        edit_author_obj.books.set(new_book_ids)
        # 3.返回
        return redirect('/author_list/')

    book_list = Book.objects.all()
    # 2.返回页面,给客户输入.
    return render(request, 'edit_author.html', {'edit_author_obj': edit_author_obj, "book_list": book_list})


def upload(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file_name')
        with open(file_obj.name, "wb") as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
    # 1.返回一个页面让客户选择 文件
    return render(request, 'upload.html')


def delete(request, table, del_id):
    print(table, del_id)
    # 方法1: 默认方法
    # table_dict = {
    #     'press': Press,
    #     'book': Book,
    #     'author': Author,
    # }
    # table_class = table_dict.get(table)
    # table_class.objects.get(id=del_id).delete()

    # 方法2: 反射器的方式
    table_class = getattr(models, table.capitalize())
    table_class.objects.get(id=del_id).delete()
    # print(table_class, type(table_class))
    return redirect(reverse(table))
