class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
    def deleteatbeg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=None
    def deleteatend(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=None
    def reverse(self):
        curr=self.head
        while curr:
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
        self.head,self.taail=self.tail,self.head
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end="->")
            temp=temp.next
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.insertatend(i)
o.printing()
print()
o.deleteatend()
o.printing()
print()
o.reverse()
o.printing()
