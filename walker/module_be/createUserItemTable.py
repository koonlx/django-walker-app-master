import random
import numpy as np
import pandas as pd

from ..models import RestaurantInfo
from pandas import DataFrame
from .timeCheckDecorator import logging_time

from django.db import connections

@logging_time
def create_categories_table(user_num: int) -> DataFrame:
    """
    - 입력받은 유저 수 만큼 "유저-카테고리" 샘플 테이블 생성.
    - 카테고리별 유저가 시켜먹은 횟수는 0~20 범위 내에서 랜덤 생성.
    - 시켜먹은 횟수는 가중치를 적용하여 숫자별로 나올 확률을 다르게 설정함.
    """
    cnt_weights = [10, 10, 10, 10] + [1] * 17
    df_value = [random.choices(range(0, 20 + 1), weights=cnt_weights, k=11) for _ in
                range(user_num)]  # 유저가 카테고리별로 시켜먹은 횟수
    df_index = ["user" + str(i) for i in range(user_num)]  # 유저 수
    df_columns = ['닭오리요리', '별식퓨전요리', '부페', '분식', '양식', '일식수산물',
                  '제과제빵떡케익', '중식', '커피점카페', '패스트푸드', '한식']  # 중분류 카테고리 11개

    df = pd.DataFrame(df_value, columns=df_columns, index=df_index)
    return df


@logging_time
def create_stores_table(user_num, curr_lat=35.8583073, curr_lon=127.026364, km=2) -> DataFrame:
    """
    - 입력받은 유저 수 만큼 "유저-전체 음식점" 샘플 테이블 생성.
    - 전체 음식점에서 시켜먹은 횟수는 0~9 범위 내에서 랜덤 생성.
    - 시켜먹은 횟수는 가중치를 적용하여 숫자별로 나올 확률을 다르게 설정함.
    - 전체 테이블을 만들면 소요 시간이 오래걸리는 관계로, 현재 좌표 기준 특정 반경 내에 있는 음식점들만 테이블로 만듦.
    """

    restaurants = RestaurantInfo.objects.select_related().filter(위도__gt=curr_lat - 2/109.958489129649955, 위도__lt=curr_lat + 2/109.958489129649955, 경도__gt=curr_lon - 2/88.74, 경도__lt=curr_lon + 2/88.74)
    # print(restaurants)
    query, params = restaurants.query.as_sql(compiler='sql_server.pyodbc.compiler.SQLCompiler', connection=connections['default'])
    df = pd.read_sql_query(query, connections['default'], params=params)
    # df = pd.DataFrame.from_records(restaurants.values())
    # df = pd.read_sql(RestaurantInfo.objects.all(), conn)
    # df = pd.read_csv("/Users/koon_9/vscode/django-projects/walker/walker/module/result.csv")
    df_columns = (distance_cal(df, curr_lat, curr_lon, km))["상호명"]
    df_index = ["user" + str(i) for i in range(user_num)]  # 유저 수
    cnt_weights = [0.5, 0.1] + [0.05] * 8
    df_value = np.random.choice(range(0, 9 + 1), (user_num, len(df_columns)), p=cnt_weights)
    df = pd.DataFrame(df_value, columns=df_columns, index=df_index)
    return df


# Haversine 기본 거리 공식을 정의함
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km


@logging_time
def distance_cal(df: DataFrame, lat, lon, km):  # 강남역 10번출구 위도, 경도
    df['distance'] = haversine(lat, lon, df['위도'].values, df['경도'].values)
    # print(df[df['distance'] < km])
    return df[df['distance'] < km]

# print(create_categories_table(100))
# print(create_stores_table(100))

# df = pd.read_csv('../result.csv')
# distance_cal(df)
