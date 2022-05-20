from operator import index


def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    start = 0
    goal = len(sorted_array)
    while goal - start >1:
        index = (start+goal)//2
        # print(start)
        if sorted_array[index] == target_number:
            return index
        elif sorted_array[index] < target_number:
            start = index
        else:
            goal = index


    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()