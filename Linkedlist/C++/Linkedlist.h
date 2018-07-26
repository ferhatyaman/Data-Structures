#ifndef LINKLIST_H_
#define LINKLIST_H_

template<class Type>
class Node;

template<class Type>
class Linkedlist
{
public:
    Linkedlist();   //Constructor
    ~Linkedlist();  //Destructor
private:
    
    Node * head;

};


template<class Type>
class Node
{
public:
    Type data;
    Node * next;
    Node(Type data, Node * next = NULL)
    {
        this->data = data;
        this->next = next;
    }
};

#endif