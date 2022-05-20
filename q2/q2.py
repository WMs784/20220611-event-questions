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

    #初期値，左端
    start = 0
    #初期値，右端
    goal = len(sorted_array)

    #真ん中の値が存在する場合
    while goal - start >1:      
        #間の値を取る
        index = (start+goal)//2
        #目標値と一致した場合
        if sorted_array[index] == target_number:
            return index
        #目標値より小さい場合
        elif sorted_array[index] < target_number:
            start = index
        #目標値より大きい場合
        else:
            goal = index

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()