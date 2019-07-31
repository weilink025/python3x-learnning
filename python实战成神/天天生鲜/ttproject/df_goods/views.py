from django.shortcuts import render
from django.http import HttpResponse,response
from faker import Factory
import random
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    producttype = ProductType.objects.all()

    # 查询类目
    fruit_type = ProductType.objects.get(pk=1)
    seafood_type = ProductType.objects.get(pk=2)
    meat_type = ProductType.objects.get(pk=3)
    egg_type = ProductType.objects.get(pk=4)
    vegetables_type = ProductType.objects.get(pk=5)
    freeze_type = ProductType.objects.get(pk=6)

    # 查询热门商品
    fruit_hot = producttype[0].productinfo_set.order_by('-pclick')[0:4]  # 水果
    seafood_hot = producttype[1].productinfo_set.order_by('-pclick')[0:4]  # 海鲜
    meat_hot = producttype[2].productinfo_set.order_by('-pclick')[0:4]  # 肉类
    egg_hot = producttype[3].productinfo_set.order_by('-pclick')[0:4]
    vegetables_hot = producttype[4].productinfo_set.order_by('-pclick')[0:4]
    freeze_hot = producttype[5].productinfo_set.order_by('-pclick')[0:4]  # 速冻食品

    # 查询推荐商品
    fruit_recommend = producttype[0].productinfo_set.filter(precommend=1)[0:4]  # 水果
    seafood_recommend = producttype[1].productinfo_set.filter(precommend=1)[0:4]  # 海鲜
    meat_recommend = producttype[2].productinfo_set.filter(precommend=1)[0:4]  # 肉类
    egg_recommend = producttype[3].productinfo_set.filter(precommend=1)[0:4]
    vegetables_recommend = producttype[4].productinfo_set.filter(precommend=1)[0:4]
    freeze_recommend = producttype[5].productinfo_set.filter(precommend=1)[0:4]  # 速冻食品

    context = {'sub_page': 1, 'title': '首页',
               'fruit_hot': fruit_hot,
               'fruit_recommend': fruit_recommend,
               'seafood_hot': seafood_hot,
               'seafood_recommend': seafood_recommend,
               'meat_hot': meat_hot,
               'meat_recommend': meat_recommend,
               'egg_hot': egg_hot,
               'egg_recommend': egg_recommend,
               'vegetables_hot': vegetables_hot,
               'vegetables_recommend': vegetables_recommend,
               'freeze_hot': freeze_hot,
               'freeze_recommend': freeze_recommend,
               'fruit_type': fruit_type,
               'seafood_type': seafood_type,
               'meat_type': meat_type,
               'egg_type': egg_type,
               'vegetables_type': vegetables_type,
               'freeze_type': freeze_type,
               }
    return render(request, 'df_goods/index.html', context)

#商品列表页面
def list(request, product_type_id):

    pro_page = request.GET.get('page')      #页数
    if pro_page == None :
        pro_page=1
    pro_sort = request.GET.get('sort')  # 排序方式

    product_type_get = ProductType.objects.get(pk=product_type_id)

    # 查询类目(菜单栏)
    producttype = ProductType.objects.all()
    fruit_type = ProductType.objects.get(pk=1)
    seafood_type = ProductType.objects.get(pk=2)
    meat_type = ProductType.objects.get(pk=3)
    egg_type = ProductType.objects.get(pk=4)
    vegetables_type = ProductType.objects.get(pk=5)
    freeze_type = ProductType.objects.get(pk=6)

    # 查询新品推荐
    product_new_get = ProductInfo.objects.filter(ptype_id=product_type_id).filter(pnew_recommend=1).order_by('-id')

    #列表分页数据
    if pro_sort == 'price_asc':    #价格升序
        product_get = ProductInfo.objects.filter(ptype_id=product_type_id).order_by('pprice')
    elif pro_sort == 'price_desc':    #价格降序
        product_get = ProductInfo.objects.filter(ptype_id=product_type_id).order_by('-pprice')
    elif pro_sort == 'click':    #访问量降序
        product_get = ProductInfo.objects.filter(ptype_id=product_type_id).order_by('-pclick')
    else:
        product_get = ProductInfo.objects.filter(ptype_id=product_type_id).order_by('-id')

    page_sum = Paginator(product_get,30)
    product_get = page_sum.page(int(pro_page))

    context = {'sub_page': 1, 'title': product_type_get,
               'fruit_type': fruit_type,
               'seafood_type': seafood_type,
               'meat_type': meat_type,
               'egg_type': egg_type,
               'vegetables_type': vegetables_type,
               'freeze_type': freeze_type,
               'product_get': product_get,  # 类目对应商品
               'product_new_get': product_new_get,  # 新品推荐
               'product_type_get': product_type_get,
               'pro_sort': pro_sort,

               }
    return render(request, 'df_goods/list.html', context)


#商品详情页面
def detail(request,product_id):
    #个人中心最近浏览商品
    pro_id_list = []
    product_id = str(product_id)
    pro_ids = request.COOKIES.get("pro_ids","")
    print(pro_ids)
    if pro_ids == "":
        pro_ids = product_id
        print(pro_ids)
    else:
        pro_id_list = pro_ids.split(',')

        if pro_id_list.count(product_id)>=1:
            pro_id_list.remove(product_id)
        pro_id_list.insert(0,product_id)

        if len(pro_id_list)>=6:
            del pro_id_list[5]
        pro_ids = ','.join(pro_id_list)


    # 查询类目(菜单栏)
    fruit_type = ProductType.objects.get(pk=1)
    seafood_type = ProductType.objects.get(pk=2)
    meat_type = ProductType.objects.get(pk=3)
    egg_type = ProductType.objects.get(pk=4)
    vegetables_type = ProductType.objects.get(pk=5)
    freeze_type = ProductType.objects.get(pk=6)

    #查询商品详情
    pro_detail = ProductInfo.objects.get( pk = product_id )
    # 点击量类加
    pro_detail.pclick = pro_detail.pclick+1
    pro_detail.save()
    pro_type_id = pro_detail.ptype_id
    pro_type = ProductType.objects.get( pk = pro_type_id )

    #查询新品推荐
    product_new_get = ProductInfo.objects.filter(ptype_id=pro_type_id).filter(pnew_recommend=1).order_by('-id')
    context = {'sub_page': 1, 'title': pro_detail,
               'fruit_type': fruit_type,
               'seafood_type': seafood_type,
               'meat_type': meat_type,
               'egg_type': egg_type,
               'vegetables_type': vegetables_type,
               'freeze_type': freeze_type,
               'pro_detail':pro_detail,
               'pro_type':pro_type,
               'product_new_get':product_new_get,
               }
    response_detail = render(request, 'df_goods/detail.html', context)
    response_detail.set_cookie("pro_ids",pro_ids)
    return response_detail








def datapool(request):
    TypeInfo_list = ProductType.objects.all()
    fake = Factory.create('zh_CN')  # 伪造数据生成器    可批量造假数据测试
    for i in range(0, 300):
        j = random.randint(0, 100)
        s1 = random.randint(0, 21)
        s2 = random.randint(0, 100)
        k = random.randint(0, 5)
        v = ProductInfo(
            pname=fake.text(max_nb_chars=10),
            ppic='df_goods/goods' + str(s1) + '.jpg',
            pprice=j,
            punit='500g',
            pclick=0,
            isDelete=fake.pybool(),  # 是否删除
            precommend=fake.pybool(),
            pnew_recommend=0,
            pbrief=fake.text(max_nb_chars=50),
            pstock=s2,
            pcontent=fake.text(max_nb_chars=1300),
            ptype=TypeInfo_list[k],  # 所属类型
        )
        v.save()
    return HttpResponse("数据伪造成功")
