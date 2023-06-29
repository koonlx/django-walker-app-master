import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import cosine_similarity
from .timeCheckDecorator import logging_time
from .createUserItemTable import create_categories_table, create_stores_table

from ..models import RestaurantInfo

def predict_cnt(user_item_matrix, item_sim_arr):
    """
    사용자별 주문 횟수 예측 함수.
    Top-N은 고려하지 않고 전체로 구현.
    ratings_arr: u x i, item_sim_arr: i x i
    """
    sum_sr = user_item_matrix @ item_sim_arr
    sum_s_abs = np.array([np.abs(item_sim_arr).sum(axis=1)])

    cnt_pred = sum_sr / sum_s_abs

    return cnt_pred


def get_mse(pred, actual):
    """
    예측 성능 평가 함수.
    성능 평가는 MSE를 사용.
    """
    # 주문 횟수가 있는 실제 주문 내역만 추출 (1차원 배열로 변환)
    pred = pred[actual.nonzero()].flatten()
    actual = actual[actual.nonzero()].flatten()

    return mean_squared_error(pred, actual)


@logging_time
def predict_rating_topsim(ratings_arr, item_sim_arr, N=20):
    # 사용자-아이템 평점 행렬 크기만큼 0으로 채운 예측 행렬 초기화
    pred = np.zeros(ratings_arr.shape)
    # pred = ratings_arr

    # 사용자-아이템 평점 행렬의 열 크기(아이템 수)만큼 반복 (row: 사용자, col: 아이템)
    for col in range(ratings_arr.shape[1]):

        # 특정 아이템의 유사도 행렬 오름차순 정렬시 index .. (1)
        temp = np.argsort(item_sim_arr[:, col])

        # (1)의 index를 역순으로 나열시 상위 N개의 index = 특정 아이템의 유사도 상위 N개 아이템 index .. (2)
        top_n_items = [temp[:-1 - N:-1]]

        # 개인화된 예측 평점을 계산: 반복당 특정 아이템의 예측 평점(사용자 전체)
        for row in range(ratings_arr.shape[0]):
            # (2)의 유사도 행렬
            item_sim_arr_topN = item_sim_arr[col, :][top_n_items].T  # N x 1

            # (2)의 실제 평점 행렬
            ratings_arr_topN = ratings_arr[row, :][top_n_items]  # 1 x N

            # 예측 평점
            pred[row, col] = ratings_arr_topN @ item_sim_arr_topN
            pred[row, col] /= np.sum(np.abs(item_sim_arr_topN))

    return pred


# 예측 높은 순서로 시리즈 반환
def recomm_categories_by_userid(pred_df, user_id):
    recomm_movies = pred_df.iloc[user_id].sort_values(ascending=False)[:]

    return recomm_movies


def CFResult():

    # order_cnt_matrix = create_categories_table(100)  # 사용자-카테고리 주문 횟수 행렬 생성
    order_cnt_matrix = create_stores_table(100)  # 사용자-전체음식점 주문 횟수 행렬 생성
    # print(order_cnt_matrix)
    order_cnt_matrix_T = order_cnt_matrix.T  # 아이템-식당 주문 횟수 행렬로 전치
    item_sim = cosine_similarity(order_cnt_matrix_T, order_cnt_matrix_T)  # 아이템 유사도 행렬
    item_sim_df = pd.DataFrame(item_sim, index=order_cnt_matrix_T.index, columns=order_cnt_matrix_T.index)  # 데이터 프레임 형태로 저장

    ratings_pred = predict_rating_topsim(order_cnt_matrix.values, item_sim_df.values, N=20)

    # 성능 평가
    # MSE2 = get_mse(ratings_pred, order_cnt_matrix.values)
    # print(f'아이템 기반 인접 TOP-6 이웃 MSE: {MSE2:.4f}')

    # 예측 평점 데이터 프레임
    ratings_pred_matrix = pd.DataFrame(data=ratings_pred, index=order_cnt_matrix.index,
                                    columns=order_cnt_matrix.columns)

    recomm_items = recomm_categories_by_userid(ratings_pred_matrix, 1)
    # print(len(ratings_pred_matrix.iloc[1].to_dict()))
    print("*"*30)
    print(recomm_items)
    return recomm_items