from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponseRedirect
from .models import RestaurantInfo, AllUsersOrderList, AllUsersOrderCount, UsersAddress
from django.contrib.auth.decorators import login_required

# import pandas as pd

from .module.collaborativeFiltering import *

temp = None
# from .module.timeCheckDecorator import logging_time

# Create your views here.

def index(request):
    """
    음식점 카테고리
    """
    return render(request, "walker/food_category.html", {})

def detail_algorithm(request):
    """
    알고리즘 결과
    """

    page = request.GET.get('page', '1')
    cfResult = CFResult()  # type Series
    cfResult_col = cfResult.keys().to_list()
    cfResult_val = cfResult.to_list()
    cfResult_list = list(zip(cfResult_col, cfResult_val))
    # restaurant_list = cfResult_list   # type: dict

    context = {"restaurant_list": cfResult_list}
    return render(request, "walker/algorithm_detail.html", context)

def detail_one(request):
    """
    카테고리 상세페이지
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    restaurant_list = RestaurantInfo.objects.filter(상권업종중분류명="닭/오리요리")

    # 페이징처리
    paginator = Paginator(restaurant_list, 14)
    page_obj = paginator.get_page(page)
    
    context = {"restaurant_list": page_obj}
    return render(request, "walker/category_detail.html", context)

def detail_two(request):
    """
    카테고리 상세페이지
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    restaurant_list = RestaurantInfo.objects.filter(상권업종중분류명="별식/퓨전요리")

    # 페이징처리
    paginator = Paginator(restaurant_list, 14)
    page_obj = paginator.get_page(page)
    
    context = {"restaurant_list": page_obj}
    return render(request, "walker/category_detail.html", context)

def detail_three(request):
    """
    카테고리 상세페이지
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    restaurant_list = RestaurantInfo.objects.filter(상권업종중분류명="부페")

    # 페이징처리
    paginator = Paginator(restaurant_list, 14)
    page_obj = paginator.get_page(page)
    
    context = {"restaurant_list": page_obj}
    return render(request, "walker/category_detail.html", context)

def detail_four(request):
    """
    카테고리 상세페이지
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    restaurant_list = RestaurantInfo.objects.filter(상권업종중분류명="분식")

    # 페이징처리
    paginator = Paginator(restaurant_list, 14)
    page_obj = paginator.get_page(page)
    
    context = {"restaurant_list": page_obj}
    return render(request, "walker/category_detail.html", context)

def detail_five(request):
    """
    카테고리 상세페이지
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    restaurant_list = RestaurantInfo.objects.filter(상권업종중분류명="양식")

    # 페이징처리
    paginator = Paginator(restaurant_list, 14)
    page_obj = paginator.get_page(page)
    
    context = {"restaurant_list": page_obj}
    return render(request, "walker/category_detail.html", context)

def detail_six(request):
    """
    카테고리 상세페이지
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    restaurant_list = RestaurantInfo.objects.filter(상권업종중분류명="일식/수산물")

    # 페이징처리
    paginator = Paginator(restaurant_list, 14)
    page_obj = paginator.get_page(page)
    
    context = {"restaurant_list": page_obj}
    return render(request, "walker/category_detail.html", context)

def detail_seven(request):
    """
    카테고리 상세페이지
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    restaurant_list = RestaurantInfo.objects.filter(상권업종중분류명="제과제빵떡케익")

    # 페이징처리
    paginator = Paginator(restaurant_list, 14)
    page_obj = paginator.get_page(page)
    
    context = {"restaurant_list": page_obj}
    return render(request, "walker/category_detail.html", context)

def detail_eight(request):
    """
    카테고리 상세페이지
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    restaurant_list = RestaurantInfo.objects.filter(상권업종중분류명="중식")

    # 페이징처리
    paginator = Paginator(restaurant_list, 14)
    page_obj = paginator.get_page(page)
    
    context = {"restaurant_list": page_obj}
    return render(request, "walker/category_detail.html", context)

def detail_nine(request):
    """
    카테고리 상세페이지
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    restaurant_list = RestaurantInfo.objects.filter(상권업종중분류명="커피점/카페")

    # 페이징처리
    paginator = Paginator(restaurant_list, 14)
    page_obj = paginator.get_page(page)
    
    context = {"restaurant_list": page_obj}
    return render(request, "walker/category_detail.html", context)

def detail_ten(request):
    """
    카테고리 상세페이지
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    restaurant_list = RestaurantInfo.objects.filter(상권업종중분류명="패스트푸드")

    # 페이징처리
    paginator = Paginator(restaurant_list, 14)
    page_obj = paginator.get_page(page)
    
    context = {"restaurant_list": page_obj}
    return render(request, "walker/category_detail.html", context)

def detail_eleven(request):
    """
    카테고리 상세페이지
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    restaurant_list = RestaurantInfo.objects.filter(상권업종중분류명="한식")

    # 페이징처리
    paginator = Paginator(restaurant_list, 14)
    page_obj = paginator.get_page(page)
    
    context = {"restaurant_list": page_obj}
    return render(request, "walker/category_detail.html", context)

@login_required(login_url="common:login")
def purchase(request):
    


    if request.method == 'POST':
        # POST 요청 처리
        restaurant_id = request.POST.get('restaurant_id')  # 버튼의 값을 가져옴

        # RestaurantInform 테이블에서 해당하는 레코드 가져오기
        restaurant_info = RestaurantInfo.objects.get(id=restaurant_id)

        # 현재 로그인한 사용자의 ID 가져오기
        user_id = request.user.id  # 로그인한 사용자의 ID를 가져오는 방법은 프로젝트에 따라 다를 수 있음

        # AllUsersOrderList 테이블에 저장
        AllUsersOrderList.objects.create(
            user_id=user_id,
            상권업종중분류명=restaurant_info.상권업종중분류명,
            상호명=restaurant_info.상호명
        )

        mapping = {
        '닭/오리요리': '닭오리요리',
        '별식/퓨전요리': '별식퓨전요리',
        '부페': '부페',
        '분식': '분식',
        '양식': '양식',
        '일식/수산물': '일식수산물',
        '제과제빵떡케익': '제과제빵떡케익',
        '중식': '중식',
        '커피점/카페': '커피점카페',
        '패스트푸드': '패스트푸드',
        '한식': '한식',
        }
        상권업종중분류명 =  restaurant_info.상권업종중분류명
        column_name = mapping.get(상권업종중분류명)

    if column_name:
        order_count, created = AllUsersOrderCount.objects.get_or_create(user_id=user_id)
        setattr(order_count, column_name, getattr(order_count, column_name) + 1)
        order_count.save()

        return HttpResponseRedirect('/walker/')  # 구매 성공 페이지로 리다이렉트

    return render(request, 'purchase.html')  # 초기 페이지 렌더링

@login_required(login_url="common:login")
def save_address(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        user_id = request.user.id
        
        # UsersAddress.objects.create(user_id=user_id, address=address)
        obj, created = UsersAddress.objects.get_or_create(user_id=user_id)

        if not created:
            obj.address = address
            obj.save()
        
        # 필요한 처리나 리디렉션 등 추가 작업 수행
        
    return render(request, 'walker/address_form.html', {})


    global temp

    temp = CFResult()
