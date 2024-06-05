class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            new=node(data)
            curr.next=new
    def deleteatbeg(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        print(temp.val)
    def deleteatend(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
            print(temp.next)
        temp.next=None
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end="->")
            temp=temp.next
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.insertatbeg(i)
o.printing()
print()
o.deleteatbeg()
o.printing()
print()
o.deleteatend()
o.printing()
print()




