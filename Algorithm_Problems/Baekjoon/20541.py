# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(list(input().split()) for _ in range(n))
        return n, board

    n, board = getdata()
    # print(board)

    class album(object) :

        # album은 이름과 하위 album리스트, 하위 file리스트로 구성되어있다.
        def __init__(self, name):
            self.name = name
            self.a = list()
            self.f = list()

        # mkalb 함수를 이용하여 name의 이름을 갖는 album을 하위 album에 추가한다.
        def mkalb(self, name):
            flag = 0
            for al in self.a :
                if name == al.name :
                    flag = 1
                    print("duplicated album name")
                    break
            if flag == 0 :
                tmp = album(name)
                self.a.append(tmp)
                # print("mk complete")

        # rmalb에서 1과 -1에서 사전 순 album제거에서 쓰일 sort함수이다.
        # 해당 album의 bool에 맞게 사전 순 빠른, 늦은 album의 index를 반환
        def albumsort(self, album, bool):
            tmp = list()
            for idx, al in enumerate(album) :
                tmp.append([idx,al.name])
            tmp.sort(key=lambda x:x[1],reverse=bool)
            return tmp[0][0]

        # -1,0,1,S에 맞게 해당 엘범을 삭제하는 함수
        # delete는 삭제하는 엘범의 하위 엘범과 파일의 개수를 반환한다.
        def rmalb(self, command):
            if command == '-1' :
                if len(self.a) != 0 :
                    idx = self.albumsort(self.a, False)
                    al_cnt, fi_cnt = self.delete(self.a[idx])
                    del self.a[idx]
                    print(al_cnt, fi_cnt)
                else :
                    print(0, 0)
            elif command == '0' :
                if len(self.a) != 0 :
                    al_cnt, fi_cnt = 0, 0
                    for al in self.a :
                        tmp1, tmp2 = self.delete(al)
                        al_cnt += tmp1
                        fi_cnt += tmp2
                    for _ in range(len(self.a)):
                        del self.a[0]
                    print(al_cnt, fi_cnt)
                else :
                    print(0, 0)
            elif command == '1' :
                if len(self.a) != 0 :
                    idx = self.albumsort(self.a, True)
                    al_cnt, fi_cnt = self.delete(self.a[idx])
                    del self.a[idx]
                    print(al_cnt, fi_cnt)
                else :
                    print(0, 0)
            else :
                flag = 0
                for idx, al in enumerate(self.a) :
                    if command == al.name :
                        flag = 1
                        al_cnt, fi_cnt = self.delete(al)
                        del self.a[idx]
                        print(al_cnt, fi_cnt)
                        break
                if flag == 0 :
                    print(0, 0)

        # 재귀를 통해 하위 엘범을 끝까지 돌며 개수를 반환
        def delete(self, album):
            al_cnt, fi_cnt = 1, 0
            for al in album.a :
                tmp1, tmp2 = self.delete(al)
                al_cnt += tmp1
                fi_cnt += tmp2
            fi_cnt += len(album.f)
            return al_cnt, fi_cnt

        # 엘범 삭제에 쓰일 소멸자
        def __del__(self):
            self.name = None
            self.a = None
            self.f = None

        # 사진을 삽입하는 함수이다.
        # 파일은 엘범과 다르므로 list에 append로 추가한다.
        def insert(self, name):
            flag = 0
            for fi in self.f:
                if name == fi :
                    flag = 1
                    print("duplicated photo name")
                    break
            if flag == 0:
                self.f.append(name)
                # print("insert complete")

        # 사진을 제거하는 함수이다.
        def deletefile(self, command):
            if command == '-1' :
                if len(self.f) != 0 :
                    self.f.sort(reverse=True)
                    self.f.pop()
                    print(1)
                else :
                    print(0)
            elif command == '0' :
                if len(self.f) != 0 :
                    print(len(self.f))
                    self.f = []
                else :
                    print(0)
            elif command == '1' :
                if len(self.f) != 0 :
                    self.f.sort(reverse=False)
                    self.f.pop()
                    print(1)
                else :
                    print(0)
            else :
                flag = 0
                for idx, fi in enumerate(self.f) :
                    if command == fi :
                        flag = 1
                        del self.f[idx]
                        print(1)
                        break
                if flag == 0 :
                    print(0)

        # 엘범 이동 함수, command에는 S만 들어오도록 main에서 조정했다.
        # main의 path를 통해 경로 이동을 저장하고 상위 엘범으로 이동할 수 있도록 한다.
        def ca(self, command):
            for al in self.a :
                if al.name == command :
                    return al
            return self

    root = album('album')
    path = list()
    cur_album = root
    # 엘범 이동 경로를 저장하여 상위 엘범으로 이동해야할 경우 사용한다.
    path.append(cur_album.name)
    # ind = 1
    for command in board :
        # print(f"=={ind}th===")
        if command[0] == 'mkalb' :
            cur_album.mkalb(command[1])
        if command[0] == 'rmalb' :
            cur_album.rmalb(command[1])
        if command[0] == 'insert' :
            cur_album.insert(command[1])
        if command[0] == 'delete':
            cur_album.deletefile(command[1])
        if command[0] == 'ca' :
            if command[1] == '/' :
                cur_album = root
                path = [cur_album.name]
                print(cur_album.name)
            elif command[1] == '..' :
                cur_album = root
                if len(path) != 1 :
                    path.pop()
                    for i in range(1, len(path)) :
                        cur_album = cur_album.ca(path[i])
                print(cur_album.name)
            else :
                cur_album = cur_album.ca(command[1])
                if cur_album.name != path[-1] :
                    path.append(cur_album.name)
                print(cur_album.name)

        # print("cont,")
        # print(path)
        # print(cur_album.name,[al.name for al in cur_album.a],cur_album.f)
        # ind += 1
