#   wap to map 2 lists into a dictionary
class Map2ListInDict:
    def map2List(self):
        l1=[1,2,3]
        l2=[5,4,7]
        d=dict()
        op=map(lambda x,y:x+y,l1,l2)
        print(list(op))

ob=Map2ListInDict()
ob.map2List()